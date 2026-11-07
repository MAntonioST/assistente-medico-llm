import json
import os
from src.agent.state import EstadoAssistente

class AgenteExames:
    def __init__(self):
        self.caminho_exames = "data/raw/exames.json"

    def processar(self, state: EstadoAssistente) -> dict:
        pergunta = state["pergunta"]

        if not os.path.exists(self.caminho_exames):
            return {"resposta_temporaria": "System Error: Lab database not found."}

        try:
            with open(self.caminho_exames, 'r', encoding='utf-8') as f:
                banco_exames = json.load(f)
        except Exception as e:
            return {"resposta_temporaria": f"Error reading lab data: {str(e)}"}

        paciente_encontrado = None
        for nome in banco_exames.keys():
            if nome.lower() in pergunta.lower():
                paciente_encontrado = nome
                break

        if paciente_encontrado:
            dados = banco_exames[paciente_encontrado]
            resposta = f"Lab Results for {paciente_encontrado} (ID: {dados.get('patient_id', 'N/A')} | Date: {dados.get('date', 'N/A')}):\n"

            for categoria, exames in dados.items():
                if isinstance(exames, dict):
                    resposta += f"\n[{categoria.replace('_', ' ').title()}]\n"
                    for exame, valor in exames.items():
                        resposta += f"  - {exame.replace('_', ' ').title()}: {valor}\n"
        else:
            resposta = "No lab results found for the patient mentioned in the query."

        return {"resposta_temporaria": resposta}
