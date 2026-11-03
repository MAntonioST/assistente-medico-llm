from src.agent.state import EstadoAssistente
from src.rag.retriever import RAGRetriever

class AgenteProtocolos:
    def __init__(self):
        self.rag = RAGRetriever()

    def processar(self, state: EstadoAssistente) -> dict:
        pergunta = state["pergunta"]

        # Busca a informação no banco de vetores (RAG)
        contexto = self.rag.buscar_contexto(pergunta)

        # Por enquanto, retornamos o contexto bruto para provar que o RAG leu o arquivo.
        # Na próxima etapa, o LLM vai ler isso e formular a resposta humana.
        resposta = f"CONTEXTO RECUPERADO DOS PROTOCOLOS:\n{contexto}\n\n(Aguardando integração com LLM para resposta final)"

        return {"resposta_temporaria": resposta}