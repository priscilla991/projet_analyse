import logging
from logging.handlers import RotatingFileHandler
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")

os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
