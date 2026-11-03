from src.agent.workflow import WorkflowAssistente

def main():
    print("Iniciando o Assistente Médico...\n")
    assistente = WorkflowAssistente()

    # Teste 1: Rota de Protocolos
    pergunta1 = "Qual o tratamento padrão para hipertensão?"
    print(f"Usuário: {pergunta1}")
    resultado1 = assistente.executar(pergunta1)
    print(f"Rota escolhida: {resultado1.get('rota')}")
    print(f"Resposta: {resultado1.get('resposta_final')}")

    print("-" * 50)

    # Teste 2: Rota de Exames
    pergunta2 = "O exame de sangue do paciente João chegou?"
    print(f"\nUsuário: {pergunta2}")
    resultado2 = assistente.executar(pergunta2)
    print(f"Rota escolhida: {resultado2.get('rota')}")
    print(f"Resposta: {resultado2.get('resposta_final')}")

if __name__ == "__main__":
    main()