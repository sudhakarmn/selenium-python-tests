import logging

def get_logger():
    logger = logging.getLogger("apiLogger")
    file_handler = logging.FileHandler("logs/automation.log")
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
