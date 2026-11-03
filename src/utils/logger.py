import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)

    # Evita duplicar logs se a função for chamada várias vezes
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Formato da mensagem: Data - Nome - Nível - Mensagem
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Handler para mostrar no terminal (Console)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Handler para salvar em arquivo (cria a pasta logs se não existir)
        os.makedirs("logs", exist_ok=True)
        file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger