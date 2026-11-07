from langgraph.graph import StateGraph, END
from src.agent.state import EstadoAssistente
from src.agent.protocol_agent import AgenteProtocolos
from src.agent.exam_agent import AgenteExames
from src.guardrails.security import GuardrailMedico

class WorkflowAssistente:
    def __init__(self, llm=None):
        self.llm = llm
        # Repassa o LLM para o agente de protocolos
        self.agente_protocolos = AgenteProtocolos(llm=self.llm)
        self.agente_exames = AgenteExames()
        self.guardrail = GuardrailMedico()

    def roteador(self, state: EstadoAssistente):
        pergunta = state["pergunta"].lower()
        # Se a pergunta falar de exames ou resultados, vai para o agente de exames
        if "exame" in pergunta or "resultado" in pergunta:
            return "agente_exames"
        return "agente_protocolos"

    def criar_grafo(self):
        workflow = StateGraph(EstadoAssistente)

        # Adicionando os nós
        workflow.add_node("agente_protocolos", self.agente_protocolos.processar)
        workflow.add_node("agente_exames", self.agente_exames.processar)
        workflow.add_node("guardrail", self.guardrail.verificar)

        # Definindo o fluxo condicional (Roteador)
        workflow.set_conditional_entry_point(
            self.roteador,
            {
                "agente_protocolos": "agente_protocolos",
                "agente_exames": "agente_exames"
            }
        )

        # Conectando os agentes ao Guardrail (saída obrigatória)
        workflow.add_edge("agente_protocolos", "guardrail")
        workflow.add_edge("agente_exames", "guardrail")
        workflow.add_edge("guardrail", END)

        return workflow.compile()
