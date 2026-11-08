import logging

logger = logging.getLogger("PendingExamsAgent")

class PendingExamsAgent:
    def __init__(self):
        # Base de dados simulada para pendências
        self.db_pendencias = {
            "robert johnson": ["Ecocardiograma", "Teste de Esforço"],
            "john doe": ["Ressonância Magnética"]
        }

    def run(self, query: str) -> str:
        logger.info(f"Analisando pendências para a query: {query}")
        query_lower = query.lower()

        for paciente, exames in self.db_pendencias.items():
            if paciente in query_lower:
                lista = ", ".join(exames)
                return f"O paciente {paciente.title()} possui os seguintes exames pendentes: {lista}."

        return "Não foram encontradas pendências de exames para o paciente informado."
