from typing import TypedDict

class EstadoAssistente(TypedDict):
    pergunta: str
    rota: str
    resposta_temporaria: str
    resposta_final: str