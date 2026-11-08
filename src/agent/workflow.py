from langgraph.graph import StateGraph, END
from typing import TypedDict
import logging

logger = logging.getLogger("Workflow")

class AgentState(TypedDict):
    query: str
    response: str
    agent_source: str

class AssistenteMedicoApp:
    def __init__(self, agente_exames, agente_protocolos, agente_pendencias, agente_alertas, guardrail):
        self.agente_exames = agente_exames
        self.agente_protocolos = agente_protocolos
        self.agente_pendencias = agente_pendencias
        self.agente_alertas = agente_alertas
        self.guardrail = guardrail
        self.graph = self._build_graph()

    def _build_graph(self):
        workflow = StateGraph(AgentState)

        workflow.add_node("roteador", self.roteador)
        workflow.add_node("exames", self.node_exames)
        workflow.add_node("protocolos", self.node_protocolos)
        workflow.add_node("pendencias", self.node_pendencias)
        workflow.add_node("alertas", self.node_alertas)
        workflow.add_node("guardrail", self.node_guardrail)

        workflow.set_entry_point("roteador")

        workflow.add_conditional_edges(
            "roteador",
            lambda x: x["agent_source"],
            {"exames": "exames", "protocolos": "protocolos", "pendencias": "pendencias", "alertas": "alertas"}
        )

        for node in ["exames", "protocolos", "pendencias", "alertas"]:
            workflow.add_edge(node, "guardrail")
        workflow.add_edge("guardrail", END)

        return workflow.compile()

    def roteador(self, state: AgentState):
        query = state["query"].lower()
        logger.info("Roteando a requisição...")

        if "pendente" in query or "falta" in query:
            state["agent_source"] = "pendencias"
        elif "alerta" in query or "aviso" in query or "emergência" in query:
            state["agent_source"] = "alertas"
        elif "exame" in query or "resultado" in query or "histórico" in query:
            state["agent_source"] = "exames"
        else:
            state["agent_source"] = "protocolos"

        return state

    def node_exames(self, state: AgentState):
        resultado = self.agente_exames.processar({"pergunta": state["query"]})
        state["response"] = resultado.get("resposta_temporaria", str(resultado))
        return state

    def node_protocolos(self, state: AgentState):
        resultado = self.agente_protocolos.processar({"pergunta": state["query"]})
        state["response"] = resultado.get("resposta_temporaria", str(resultado))
        return state

    def node_pendencias(self, state: AgentState):
        state["response"] = self.agente_pendencias.run(state["query"])
        return state

    def node_alertas(self, state: AgentState):
        state["response"] = self.agente_alertas.run(state["query"])
        return state

    def node_guardrail(self, state: AgentState):
        # Chama o método verificar da sua classe GuardrailMedico
        resultado = self.guardrail.verificar({"resposta_temporaria": state["response"]})
        state["response"] = resultado.get("resposta_final", state["response"])
        return state

    def processar(self, query: str) -> str:
        state = {"query": query, "response": "", "agent_source": ""}
        result = self.graph.invoke(state)
        return result["response"]

    def get_graph(self):
        return self.graph
