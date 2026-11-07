import json
from src.agent.state import EstadoAssistente

class AgenteExames:
    def __init__(self):
        self.db_path = "data/raw/exames.json"

    def processar(self, state: EstadoAssistente) -> dict:
        print("   👩‍🔬 Dra. Exames (Laboratório): Buscando os laudos mais recentes no sistema...")
        pergunta = state["pergunta"].lower()

        # Identifica o paciente na pergunta
        pacientes_conhecidos = ["john doe", "jane smith", "robert johnson", "emily chen", "michael brown"]
        paciente_alvo = next((p for p in pacientes_conhecidos if p in pergunta), None)

        if not paciente_alvo:
            return {"resposta_temporaria": "Não consegui identificar o nome do paciente na solicitação de exames."}

        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                exames = json.load(f)

            # Busca direta e limpa, pois o JSON agora está padronizado
            resultados = [ex for ex in exames if ex.get("patient_name", "").lower() == paciente_alvo]

            if not resultados:
                return {"resposta_temporaria": f"Nenhum exame encontrado para o paciente {paciente_alvo.title()}."}

            exame = resultados[0]
            resposta = f"🔬 **Resultados Laboratoriais para {exame.get('patient_name')}** (ID: {exame.get('patient_id')} | Data: {exame.get('date')}):\n\n"

            if "blood_count" in exame:
                resposta += "[Hemograma]\n"
                resposta += f"  - Hemoglobina: {exame['blood_count'].get('hemoglobin', 'N/A')} g/dL\n"
                resposta += f"  - Status: {exame['blood_count'].get('status', 'N/A').replace('Normal', 'Normal')}\n\n"

            if "lipid_panel" in exame:
                resposta += "[Perfil Lipídico]\n"
                resposta += f"  - Colesterol LDL: {exame['lipid_panel'].get('ldl_cholesterol', 'N/A')} mg/dL\n"
                resposta += f"  - Status: {exame['lipid_panel'].get('status', 'N/A').replace('Borderline', 'Limítrofe')}\n\n"

            if "metabolic_panel" in exame:
                resposta += "[Painel Metabólico]\n"
                resposta += f"  - Glicose em Jejum: {exame['metabolic_panel'].get('fasting_glucose', 'N/A')} mg/dL\n"
                resposta += f"  - Status: {exame['metabolic_panel'].get('status', 'N/A').replace('High (Diabetes Risk)', 'Alto (Risco de Diabetes)')}\n\n"

            if "hba1c" in exame:
                resposta += "[Hemoglobina Glicada (HbA1c)]\n"
                resposta += f"  - Valor: {exame['hba1c'].get('value', 'N/A')}\n"
                resposta += f"  - Status: {exame['hba1c'].get('status', 'N/A').replace('High', 'Alto')}\n"

            return {"resposta_temporaria": resposta.strip()}

        except Exception as e:
            return {"resposta_temporaria": f"Erro ao acessar o banco de exames: {str(e)}"}
