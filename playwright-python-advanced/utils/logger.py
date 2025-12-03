import logging
from logging.handlers import RotatingFileHandler
import os


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name=__name__):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger


    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")


    fh = RotatingFileHandler(os.path.join(LOG_DIR, "tests.log"), maxBytes=5_000_000, backupCount=3)
    fh.setFormatter(fmt)


    sh = logging.StreamHandler()
    sh.setFormatter(fmt)


    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger