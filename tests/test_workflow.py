from src.agent.workflow import WorkflowAssistente

def test_roteamento_para_protocolos():
    workflow = WorkflowAssistente()
    estado_teste = {"pergunta": "Qual o protocolo de tratamento para asma?"}

    resultado = workflow.roteador(estado_teste)

    # Agora verificamos o valor dentro do dicionário
    assert resultado["rota"] == "agente_protocolos"

def test_roteamento_para_exames():
    workflow = WorkflowAssistente()
    estado_teste = {"pergunta": "Pode verificar o exame de glicemia do paciente?"}

    resultado = workflow.roteador(estado_teste)

    # Agora verificamos o valor dentro do dicionário
    assert resultado["rota"] == "agente_exames"