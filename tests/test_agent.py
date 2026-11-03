from src.agent.state import EstadoAssistente
from src.agent.exam_agent import AgenteExames
from src.agent.protocol_agent import AgenteProtocolos

def test_agente_exames_retorna_mock():
    # Testa se o agente de exames devolve a estrutura correta mesmo com dados fictícios
    agente = AgenteExames()
    estado_teste = {"pergunta": "Como está o exame de sangue do João?"}

    resultado = agente.processar(estado_teste)

    assert "resposta_temporaria" in resultado
    assert "exame de sangue" in resultado["resposta_temporaria"]
    assert "não constam alterações" in resultado["resposta_temporaria"]

def test_agente_protocolos_integra_rag():
    # Testa se o agente de protocolos consegue acionar o RAG com sucesso
    agente = AgenteProtocolos()
    estado_teste = {"pergunta": "Qual o tratamento para hipertensão?"}

    resultado = agente.processar(estado_teste)

    assert "resposta_temporaria" in resultado
    assert "CONTEXTO RECUPERADO" in resultado["resposta_temporaria"]