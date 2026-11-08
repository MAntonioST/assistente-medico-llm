from src.agent.state import EstadoAssistente

class GuardrailMedico:
    def verificar(self, state: EstadoAssistente) -> dict:
        print("   [Guardrail] 🛡️ Aplicando travas de segurança e avisos médicos...")
        resposta_temporaria = state.get("resposta_temporaria", "")

        aviso = "\n\n⚠️ AVISO DE SEGURANÇA: Esta é uma análise gerada por IA. Não prescreva medicamentos ou tratamentos sem a validação humana de um médico responsável."
        resposta_final = resposta_temporaria + aviso

        return {"resposta_final": resposta_final}
