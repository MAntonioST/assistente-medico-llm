import os

def verificar_arquivo(caminho, palavras_chave):
    if not os.path.exists(caminho):
        return False, "Arquivo não encontrado."

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            faltando = [palavra for palavra in palavras_chave if palavra not in conteudo]

            if faltando:
                return False, f"Desatualizado. Faltam os termos: {', '.join(faltando)}"
            return True, "Atualizado e correto."
    except Exception as e:
        return False, f"Erro ao ler o arquivo: {str(e)}"

def rodar_verificacao():
    arquivos_criticos = {
        "src/agent/workflow.py": ["StateGraph", "roteador", "agente_exames"],
        "src/agent/protocol_agent.py": ["RAGRetriever", "llm.invoke", "CONTEXTO RECUPERADO"],
        "data/raw/protocolo_hipertensao.txt": ["hipertensão", "Enalapril"],
        "README.md": ["LangGraph", "Tech Challenge"]
    }

    print("\n=== VERIFICAÇÃO DE INTEGRIDADE DO PROJETO ===\n")

    tudo_certo = True
    for caminho, palavras_chave in arquivos_criticos.items():
        status, mensagem = verificar_arquivo(caminho, palavras_chave)
        if status:
            print(f"✅ {caminho}: {mensagem}")
        else:
            print(f"❌ {caminho}: {mensagem}")
            tudo_certo = False

    print("\n=============================================\n")

    if tudo_certo:
        print("🎉 SUCESSO: Seu projeto local está idêntico ao do Colab e pronto para evoluir!")
    else:
        print("⚠️ ATENÇÃO: Alguns arquivos estão desatualizados ou ausentes.")
        print("Copie o código final que geramos no Colab para os arquivos marcados com ❌.")

if __name__ == '__main__':
    rodar_verificacao()
