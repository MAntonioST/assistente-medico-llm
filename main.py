import logging
import sys
from src.agent.workflow import AssistenteMedicoApp
from src.agent.exam_agent import AgenteExames
from src.agent.protocol_agent import AgenteProtocolos
from src.agent.pending_agent import PendingExamsAgent
from src.agent.alert_agent import AlertAgent
from src.guardrails.medical_guardrail import GuardrailMedico

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout)])

def main():
    print("Inicializando o Assistente Médico Multiagentes...")

    agente_exames = AgenteExames()
    agente_protocolos = AgenteProtocolos(llm=None)
    agente_pendencias = PendingExamsAgent()
    agente_alertas = AlertAgent()
    guardrail = GuardrailMedico()

    app = AssistenteMedicoApp(agente_exames, agente_protocolos, agente_pendencias, agente_alertas, guardrail)

    print("\n✅ Sistema pronto! Digite sua pergunta (ou 'sair' para encerrar).")
    print("Experimente: 'exames pendentes do robert johnson' ou 'emitir alerta de emergência'.")

    while True:
        pergunta = input("\n👨‍⚕️ Usuário: ")
        if pergunta.lower() in ['sair', 'exit', 'quit', 'q']:
            break
        resposta = app.processar(pergunta)
        print(f"🤖 Assistente: {resposta}")

if __name__ == "__main__":
    main()
