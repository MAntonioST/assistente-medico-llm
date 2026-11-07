from src.agent.state import EstadoAssistente

class GuardrailMedico:
    def verificar(self, state: EstadoAssistente) -> dict:
        # Pega a resposta gerada pelos agentes anteriores
        resposta_temporaria = state.get("resposta_temporaria", "")

        # Adiciona a trava de segurança obrigatória
        aviso = "\n\n⚠️ AVISO DE SEGURANÇA: Esta é uma análise gerada por IA. Não prescreva medicamentos ou tratamentos sem a validação humana de um médico responsável."

        resposta_final = resposta_temporaria + aviso

        # Retorna a resposta final para o LangGraph encerrar o fluxo
        return {"resposta_final": resposta_final}
