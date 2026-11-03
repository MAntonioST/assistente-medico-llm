from src.guardrails.security import GuardrailMedico

def test_aviso_seguranca_presente():
    # 1. Configuração (Setup)
    guardrail = GuardrailMedico()
    # Agora passamos um dicionário simulando o estado do LangGraph
    estado_teste = {"resposta_temporaria": "O tratamento recomendado é repouso e hidratação."}

    # 2. Ação (Action)
    resultado = guardrail.validar_resposta(estado_teste)

    # 3. Verificação (Assert)
    assert "O tratamento recomendado é repouso e hidratação." in resultado["resposta_final"]
    assert "AVISO DE SEGURANÇA" in resultado["resposta_final"]