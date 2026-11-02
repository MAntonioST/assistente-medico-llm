import logging
from typing import Dict, Any
from datasets import load_dataset
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Configuração de log (Boas práticas de engenharia)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MedicalDataPreprocessor:
    """
    Classe responsável por carregar, limpar e anonimizar datasets médicos.
    """
    def __init__(self):
        logger.info("Inicializando motores de anonimização (Presidio)...")
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def anonymize_text(self, text: str) -> str:
        """
        Remove dados sensíveis (PII) como nomes, locais e documentos do texto.
        """
        if not text:
            return ""

        # Analisa o texto em busca de entidades sensíveis
        results = self.analyzer.analyze(text=text, entities=["PERSON", "LOCATION", "PHONE_NUMBER", "EMAIL_ADDRESS"], language='en')

        # Substitui as entidades encontradas por tags (ex: <PERSON>)
        anonymized_result = self.anonymizer.anonymize(text=text, analyzer_results=results)
        return anonymized_result.text

    def load_and_prepare_pubmedqa(self) -> Any:
        """
        Carrega o dataset PubMedQA sugerido na Fase 3 e aplica a anonimização.
        """
        logger.info("Baixando dataset PubMedQA...")
        # Usamos a versão 'pqa_labeled' que contém perguntas e respostas validadas
        dataset = load_dataset("pubmed_qa", "pqa_labeled", split="train", trust_remote_code=True)

        logger.info(f"Dataset carregado com {len(dataset)} registros. Iniciando anonimização...")

        def process_batch(batch: Dict[str, list]) -> Dict[str, list]:
            # Anonimiza as perguntas e as conclusões (respostas)
            batch["question"] = [self.anonymize_text(q) for q in batch["question"]]
            batch["long_answer"] = [self.anonymize_text(a) for a in batch["long_answer"]]
            return batch

        # Aplica a transformação em lote para maior performance
        processed_dataset = dataset.map(process_batch, batched=True, batch_size=100)
        logger.info("Pré-processamento e anonimização concluídos com sucesso!")

        return processed_dataset

if __name__ == "__main__":
    # Teste rápido do módulo
    preprocessor = MedicalDataPreprocessor()
    dataset_limpo = preprocessor.load_and_prepare_pubmedqa()
    print("\nExemplo de dado processado:")
    print(dataset_limpo[0])