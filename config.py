import os

class ConfigurationError(Exception):
    pass

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
EXCHANGE_NAME = os.getenv('EXCHANGE_NAME')

TRADING_PAIR = 'BTC/USDT'
GRID_MIN_PRICE = 30000
GRID_MAX_PRICE = 40000
NUMBER_OF_GRIDS = 10
ORDER_SIZE = 0.01

if not all([API_KEY, API_SECRET, EXCHANGE_NAME]):
    raise ConfigurationError("Missing required API configuration parameters.")
