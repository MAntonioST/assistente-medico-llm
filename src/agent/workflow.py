from langgraph.graph import StateGraph, END
from src.agent.state import EstadoAssistente
from src.agent.protocol_agent import AgenteProtocolos
from src.agent.exam_agent import AgenteExames
from src.guardrails.security import GuardrailMedico

class WorkflowAssistente:
    def __init__(self, llm=None):
        self.llm = llm
        self.agente_protocolos = AgenteProtocolos(llm=self.llm)
        self.agente_exames = AgenteExames()
        self.guardrail = GuardrailMedico()

    def roteador(self, state: EstadoAssistente):
        pergunta = state["pergunta"].lower()
        print("   [Roteador] 🧭 Analisando a intenção da pergunta...")

        if "exame" in pergunta or "resultado" in pergunta:
            print("   [Roteador] ➡️ Direcionando para o Agente de Exames.")
            return "agente_exames"

        print("   [Roteador] ➡️ Direcionando para o Agente de Protocolos.")
        return "agente_protocolos"

    def criar_grafo(self):
        workflow = StateGraph(EstadoAssistente)

        workflow.add_node("agente_protocolos", self.agente_protocolos.processar)
        workflow.add_node("agente_exames", self.agente_exames.processar)
        workflow.add_node("guardrail", self.guardrail.verificar)

        workflow.set_conditional_entry_point(
            self.roteador,
            {
                "agente_protocolos": "agente_protocolos",
                "agente_exames": "agente_exames"
            }
        )

        workflow.add_edge("agente_protocolos", "guardrail")
        workflow.add_edge("agente_exames", "guardrail")
        workflow.add_edge("guardrail", END)

        return workflow.compile()
