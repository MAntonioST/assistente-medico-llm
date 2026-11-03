from langgraph.graph import StateGraph, END
from typing import Literal
from src.agent.state import EstadoAssistente
from src.agent.protocol_agent import AgenteProtocolos
from src.agent.exam_agent import AgenteExames
from src.guardrails.security import GuardrailMedico

class WorkflowAssistente:
    def __init__(self):
        self.agente_protocolos = AgenteProtocolos()
        self.agente_exames = AgenteExames()
        self.guardrail = GuardrailMedico()
        self.grafo = self._montar_grafo()

    def roteador(self, state: EstadoAssistente) -> dict:
        pergunta = state["pergunta"].lower()
        if "exame" in pergunta or "sangue" in pergunta or "raio-x" in pergunta:
            return {"rota": "agente_exames"}
        return {"rota": "agente_protocolos"}

    def decidir_proximo_passo(self, state: EstadoAssistente) -> Literal["agente_protocolos", "agente_exames"]:
        return state["rota"]

    def _montar_grafo(self):
        workflow = StateGraph(EstadoAssistente)

        # Adiciona os nós chamando os métodos das classes
        workflow.add_node("roteador", self.roteador)
        workflow.add_node("agente_protocolos", self.agente_protocolos.processar)
        workflow.add_node("agente_exames", self.agente_exames.processar)
        workflow.add_node("guardrail", self.guardrail.validar_resposta)

        # Define as arestas (caminhos)
        workflow.set_entry_point("roteador")
        workflow.add_conditional_edges("roteador", self.decidir_proximo_passo)
        workflow.add_edge("agente_protocolos", "guardrail")
        workflow.add_edge("agente_exames", "guardrail")
        workflow.add_edge("guardrail", END)

        return workflow.compile()

    def executar(self, pergunta: str) -> dict:
        return self.grafo.invoke({"pergunta": pergunta})