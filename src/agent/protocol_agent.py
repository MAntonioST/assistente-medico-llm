from src.agent.state import EstadoAssistente
from src.rag.retriever import RAGRetriever

class AgenteProtocolos:
    def __init__(self, llm=None):
        self.rag = RAGRetriever()
        self.llm = llm

    def processar(self, state: EstadoAssistente) -> dict:
        print("   👨‍🏫 Dr. Protocolos (Especialista): Entendido! Consultando a biblioteca médica e os prontuários no nosso banco vetorial...")
        pergunta = state["pergunta"]

        contexto_bruto = self.rag.buscar_contexto(pergunta, k=5)

        chunks = contexto_bruto.split("\n\n")
        chunks_relevantes = []

        # Limpa a pontuação e divide a pergunta em palavras exatas
        palavras_pergunta = pergunta.lower().replace("?", "").replace(".", "").replace(",", "").split()

        for chunk in chunks:
            chunk_lower = chunk.lower()

            # Regra 1: Se for um prontuário de paciente
            if "paciente:" in chunk_lower:
                primeira_linha = chunk_lower.split('\n')[0]
                nome_paciente = primeira_linha.replace("paciente:", "").strip()
                partes_nome = [p for p in nome_paciente.split() if len(p) > 2]

                # Só adiciona se o nome for uma palavra exata na pergunta
                if any(parte in palavras_pergunta for parte in partes_nome):
                    if chunk not in chunks_relevantes:
                        chunks_relevantes.append(chunk)

            # Regra 2: Se não for prontuário (é protocolo/diretriz)
            else:
                if chunk not in chunks_relevantes:
                    chunks_relevantes.append(chunk)

        if not chunks_relevantes:
            chunks_relevantes = chunks[:2]

        contexto_final = "\n\n".join(chunks_relevantes)

        if self.llm:
            prompt = f"<|system|>\nYou are a medical assistant. Answer based ONLY on the context.</s>\n<|user|>\nContext: {contexto_final}\nQuestion: {pergunta}</s>\n<|assistant|>\n"
            resposta = self.llm.invoke(prompt)
        else:
            resposta = "🔍 [MODO LOCAL - LLM DESATIVADA]\n"
            resposta += "Documentos filtrados pelo Agente (Filtro Pós-Busca) para análise:\n\n"
            for i, chunk in enumerate(chunks_relevantes, 1):
                if chunk.strip():
                    resposta += f"--- Documento {i} ---\n{chunk.strip()}\n\n"
            resposta += "*(Nota: O Agente aplicou um filtro inteligente para remover prontuários de outros pacientes antes de enviar à LLM.)*"

        return {"resposta_temporaria": resposta}
