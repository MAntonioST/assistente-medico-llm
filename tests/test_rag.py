import os
from src.rag.retriever import RAGRetriever

def test_rag_carrega_documento():
    # Verifica se o arquivo de texto realmente existe onde deveria
    caminho_arquivo = "data/raw/protocolo_hipertensao.txt"
    assert os.path.exists(caminho_arquivo), "Arquivo de protocolo não encontrado!"

    # Inicializa o RAG e faz uma busca de teste
    rag = RAGRetriever(data_path=caminho_arquivo)
    contexto = rag.buscar_contexto("hipertensão")

    # Verifica se o RAG retornou um texto válido e não vazio
    assert isinstance(contexto, str)
    assert len(contexto) > 0
    assert "DIAGNÓSTICO" in contexto or "TRATAMENTO" in contexto