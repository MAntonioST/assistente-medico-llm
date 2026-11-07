import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class RAGRetriever:
    def __init__(self):
        self.data_dir = "data/raw"
        self.persist_dir = "data/vector_db"

        # Modelo leve de embeddings para rodar na CPU local
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )

        self.vector_store = self._init_vector_store()

    def _init_vector_store(self):
        # Se o banco já existe, carrega da memória
        if os.path.exists(self.persist_dir) and os.listdir(self.persist_dir):
            print("   [RAG] 🗄️ Carregando banco vetorial existente...")
            return Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embeddings
            )

        print("   [RAG] ⚙️ Lendo arquivos .txt e criando novo banco vetorial...")
        documentos = []

        # Lê todos os arquivos .txt do diretório
        for arquivo in os.listdir(self.data_dir):
            if arquivo.endswith(".txt"):
                caminho = os.path.join(self.data_dir, arquivo)
                try:
                    loader = TextLoader(caminho, encoding="utf-8")
                    documentos.extend(loader.load())
                except Exception as e:
                    print(f"   [RAG] ⚠️ Erro ao ler {arquivo}: {e}")

        # Quebra os textos em pedaços menores (chunks)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = text_splitter.split_documents(documentos)

        # Cria e salva o banco vetorial
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_dir
        )
        return vector_store

    def buscar_contexto(self, pergunta: str, k: int = 3) -> str:
        # Busca os k chunks mais relevantes
        resultados = self.vector_store.similarity_search(pergunta, k=k)
        contexto = "\n\n".join([doc.page_content for doc in resultados])
        return contexto
