import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger('ai_grid_trader')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler('trader.log', maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
