from src.agent.state import EstadoAssistente
from src.rag.retriever import RAGRetriever

class AgenteProtocolos:
    def __init__(self, llm=None):
        self.rag = RAGRetriever()
        self.llm = llm

    def processar(self, state: EstadoAssistente) -> dict:
        pergunta = state["pergunta"]
        contexto = self.rag.buscar_contexto(pergunta)

        if self.llm:
            prompt = f"<|system|>\nYou are a medical assistant. Answer based ONLY on the context.</s>\n<|user|>\nContext: {contexto}\nQuestion: {pergunta}</s>\n<|assistant|>\n"
            resposta = self.llm.invoke(prompt)
        else:
            resposta = f"CONTEXTO RECUPERADO:\n{contexto}\n\n(Sem LLM)"

        return {"resposta_temporaria": resposta}
