import logging

logger = logging.getLogger("AlertAgent")

class AlertAgent:
    def __init__(self):
        pass

    def run(self, query: str) -> str:
        logger.info(f"Gerando alerta para a query: {query}")
        return f"⚠️ ALERTA ENVIADO À EQUIPE MÉDICA: Atenção requerida para a situação descrita. Por favor, revisar o prontuário imediatamente. Fonte: Sistema de Monitoramento Automático."
