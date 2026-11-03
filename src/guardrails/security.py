from src.agent.state import EstadoAssistente

class GuardrailMedico:
    def __init__(self):
        self.aviso_legal = "\n\n⚠️ AVISO DE SEGURANÇA: Esta é uma análise gerada por IA. Não prescreva medicamentos ou tratamentos sem a validação humana de um médico responsável."

    def validar_resposta(self, state: EstadoAssistente) -> dict:
        resposta = state.get("resposta_temporaria", "")
        return {"resposta_final": resposta + self.aviso_legal}