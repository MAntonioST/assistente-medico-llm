import os
import sys
import importlib

def check_project():
    print("=== Verificação de Integridade do Projeto ===\n")

    # 1. Checar Ambiente Virtual (venv)
    print("[1] Verificando Ambiente...")
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Ambiente Virtual (venv): Ativo")
    else:
        print("❌ Ambiente Virtual (venv): INATIVO (Ative antes de rodar!)")

    # 2. Checar Estrutura de Pastas
    print("\n[2] Verificando Estrutura de Pastas...")
    pastas = [
        "src/agent", "src/rag", "src/guardrails", "src/utils",
        "data/raw", "data/vector_db", "tests", "assets"
    ]
    for pasta in pastas:
        if os.path.exists(pasta):
            print(f"✅ Pasta '{pasta}' encontrada.")
        else:
            print(f"⚠️ Pasta '{pasta}' ausente (Crie se for utilizar).")

    # 3. Checar Arquivos Críticos
    print("\n[3] Verificando Arquivos Críticos...")
    arquivos = [
        "data/raw/protocolo_hipertensao.txt",
        "requirements.txt",
        "main.py",
        ".gitignore"
    ]
    for arq in arquivos:
        if os.path.exists(arq):
            print(f"✅ Arquivo '{arq}' encontrado.")
        else:
            print(f"❌ Arquivo '{arq}' ausente!")

    # 4. Checar Bibliotecas Principais
    print("\n[4] Verificando Bibliotecas...")
    libs = {
        "langgraph": "langgraph",
        "langchain_core": "langchain-core",
        "langchain_chroma": "langchain-chroma",
        "sentence_transformers": "sentence-transformers"
    }
    for modulo, nome_pip in libs.items():
        try:
            importlib.import_module(modulo)
            print(f"✅ Biblioteca '{nome_pip}' instalada e acessível.")
        except ImportError:
            print(f"❌ Biblioteca '{nome_pip}' ausente! Rode: pip install {nome_pip}")

    print("\n=============================================")
    print("Verificação concluída!")

if __name__ == "__main__":
    check_project()