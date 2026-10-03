import os
import re
from pathlib import Path

# Configurações base
BASE_DIR = Path(__file__).resolve().parent
REQUIRED_DIRS = [
    "data/raw", "data/processed", "data/vector_db",
    "src/data_prep", "src/fine_tuning", "src/rag", 
    "src/agent", "src/guardrails", "src/utils", "tests"
]
REQUIRED_FILES = ["README.md", "requirements.txt", ".env", "main.py"]

# Regex básicos para detectar dados sensíveis (PII) que precisam de anonimização
PII_PATTERNS = {
    "CPF": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
    "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "Telefone": r"\b|$\d{2}$|\s\d{4,5}-\d{4}\b"
}

def check_directories():
    print("\n🔍 1. Verificando Estrutura de Diretórios (Modularização)...")
    missing = []
    for d in REQUIRED_DIRS:
        path = BASE_DIR / d
        if not path.exists():
            missing.append(d)

    if missing:
        print("❌ Faltam os seguintes diretórios (Corrija criando-os):")
        for m in missing: print(f"   - {m}")
    else:
        print("✅ Estrutura de diretórios OK (Padrão SOLID mantido).")

def check_files():
    print("\n🔍 2. Verificando Arquivos Obrigatórios...")
    missing = []
    for f in REQUIRED_FILES:
        path = BASE_DIR / f
        if not path.exists():
            missing.append(f)

    if missing:
        print("❌ Faltam os seguintes arquivos base:")
        for m in missing: print(f"   - {m}")
    else:
        print("✅ Arquivos base OK.")

def check_dependencies():
    print("\n🔍 3. Verificando Dependências (requirements.txt)...")
    req_path = BASE_DIR / "requirements.txt"
    if not req_path.exists():
        print("⚠️ Arquivo requirements.txt não encontrado para análise.")
        return

    with open(req_path, "r", encoding="utf-8") as f:
        content = f.read().lower()

    required_libs = ["langchain", "langgraph", "transformers", "peft", "torch"]
    missing_libs = [lib for lib in required_libs if lib not in content]

    if missing_libs:
        print("⚠️ Atenção: Para a Fase 3, adicione as seguintes bibliotecas no requirements.txt:")
        for lib in missing_libs: print(f"   - {lib}")
    else:
        print("✅ Dependências principais mapeadas.")

def analyze_data_anonymization():
    print("\n🔍 4. Analisando Necessidade de Anonimização nos Dados Brutos...")
    raw_dir = BASE_DIR / "data/raw"
    if not raw_dir.exists() or not any(raw_dir.iterdir()):
        print("⚠️ Nenhum dataset encontrado em 'data/raw/'.")
        print("   -> Lembrete: Baixe o PubMedQA ou MedQuAD conforme sugerido no PDF.")
        return

    found_pii = False
    for file_path in raw_dir.glob("*.*"):
        if file_path.suffix in [".csv", ".json", ".txt"]:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    for pii_type, pattern in PII_PATTERNS.items():
                        matches = re.findall(pattern, content)
                        if matches:
                            found_pii = True
                            print(f"❌ ALERTA DE SEGURANÇA: {len(matches)} ocorrências de {pii_type} encontradas no arquivo {file_path.name}.")
            except Exception as e:
                print(f"Erro ao ler {file_path.name}: {e}")

    if found_pii:
        print("   -> Ação Necessária: O módulo 'src/data_prep' deve aplicar regex ou bibliotecas como Presidio para anonimizar esses dados antes do Fine-Tuning.")
    else:
        print("✅ Nenhuma violação óbvia de PII encontrada ou dados ainda não inseridos.")

def main():
    print("="*60)
    print("🏥 HEALTH CHECK - ASSISTENTE MÉDICO LLM (FASE 3) 🏥")
    print("="*60)
    check_directories()
    check_files()
    check_dependencies()
    analyze_data_anonymization()
    print("\n" + "="*60)
    print("🚀 Análise concluída. Verifique os alertas acima para correções.")

if __name__ == "__main__":
    main()