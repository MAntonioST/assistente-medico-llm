import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class RAGRetriever:
    def __init__(self, data_path="data/raw/protocolo_hipertensao.txt", persist_dir="data/vector_db"):
        self.data_path = data_path
        self.persist_dir = persist_dir
        # Usamos um modelo leve e open-source para rodar rápido na sua máquina
        self.embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)
        self.vector_store = self._init_vector_store()

    def _init_vector_store(self):
        # Se o banco já existe, apenas carrega
        if os.path.exists(self.persist_dir) and os.listdir(self.persist_dir):
            return Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)

        # Caso contrário, lê o arquivo, divide e cria o banco vetorial
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.data_path}")

        loader = TextLoader(self.data_path, encoding="utf-8")
        documentos = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        textos_divididos = text_splitter.split_documents(documentos)

        vector_store = Chroma.from_documents(
            documents=textos_divididos,
            embedding=self.embeddings,
            persist_directory=self.persist_dir
        )
        return vector_store

    def buscar_contexto(self, query: str, k: int = 2) -> str:
        # Busca os trechos mais relevantes para a pergunta
        resultados = self.vector_store.similarity_search(query, k=k)
        contexto = "\n".join([doc.page_content for doc in resultados])
        return contexto