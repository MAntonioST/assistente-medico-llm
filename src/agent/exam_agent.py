from src.agent.state import EstadoAssistente

class AgenteExames:
    def __init__(self):
        pass

    def processar(self, state: EstadoAssistente) -> dict:
        resposta = f"Analisando o histórico de exames para a dúvida '{state['pergunta']}', não constam alterações críticas recentes."
        return {"resposta_temporaria": resposta}