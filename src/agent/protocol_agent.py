from src.agent.state import EstadoAssistente

class AgenteProtocolos:
    def __init__(self):
        # Futuramente, aqui instanciaremos o modelo RAG
        pass

    def processar(self, state: EstadoAssistente) -> dict:
        resposta = f"Baseado nos protocolos médicos para a queixa '{state['pergunta']}', o procedimento padrão indica avaliação clínica detalhada."
        return {"resposta_temporaria": resposta}