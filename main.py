from src.agent.workflow import WorkflowAssistente

def main():
    print("\n" + "="*60)
    print("🏥 INICIANDO O ASSISTENTE MÉDICO (FIAP - Fase 3)")
    print("="*60 + "\n")

    # Inicializa o workflow (passando llm=None para não travar a máquina local)
    workflow = WorkflowAssistente(llm=None)
    app = workflow.criar_grafo()

    # Novas perguntas baseadas no nosso banco JSON atualizado
    perguntas_teste = [
        "Qual o tratamento padrão para hipertensão?",
        "O exame de sangue do paciente Robert Johnson chegou?"
    ]

    for pergunta in perguntas_teste:
        print(f"👤 USUÁRIO: {pergunta}")

        # Executa o grafo
        resultado = app.invoke({"pergunta": pergunta})

        print(f"\n🤖 ASSISTENTE:")
        print(f"{resultado['resposta_final']}\n")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()
