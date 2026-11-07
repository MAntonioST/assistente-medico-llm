from src.agent.state import EstadoAssistente
from src.rag.retriever import RAGRetriever

class AgenteProtocolos:
    def __init__(self, llm=None):
        self.rag = RAGRetriever()
        self.llm = llm

    def processar(self, state: EstadoAssistente) -> dict:
        print("   [Agente de Protocolos] 📚 Buscando diretrizes no banco vetorial (RAG)...")
        pergunta = state["pergunta"]
        contexto = self.rag.buscar_contexto(pergunta)

        if self.llm:
            prompt = f"<|system|>\nYou are a medical assistant. Answer based ONLY on the context.</s>\n<|user|>\nContext: {contexto}\nQuestion: {pergunta}</s>\n<|assistant|>\n"
            resposta = self.llm.invoke(prompt)
        else:
            resposta = "Com base nas diretrizes clínicas recuperadas da base de dados:\n\n"
            resposta += f"{contexto}\n\n"
            resposta += "*(Nota do Sistema: Resposta extraída via RAG. LLM desativada no ambiente local)*"

        return {"resposta_temporaria": resposta}
