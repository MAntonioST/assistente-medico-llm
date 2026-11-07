from src.agent.workflow import WorkflowAssistente

def main():
    print("\n" + "="*60)
    print("🏥 INICIANDO O ASSISTENTE MÉDICO (FIAP - Fase 3)")
    print("="*60 + "\n")

    workflow = WorkflowAssistente(llm=None)
    app = workflow.criar_grafo()

    # Adicionamos uma pergunta sobre o histórico do paciente!
    perguntas_teste = [
        "Qual o tratamento padrão para hipertensão?",
        "O exame de sangue do paciente Robert Johnson chegou?",
        "Qual o histórico clínico do paciente Robert Johnson?"
    ]

    for pergunta in perguntas_teste:
        print(f"👤 USUÁRIO: {pergunta}")
        resultado = app.invoke({"pergunta": pergunta})
        print(f"\n🤖 ASSISTENTE:\n{resultado['resposta_final']}\n")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()
