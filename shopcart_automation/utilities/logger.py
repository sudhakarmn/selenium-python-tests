import logging

def logger():
    logging.basicConfig(
        filename="automation.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()
