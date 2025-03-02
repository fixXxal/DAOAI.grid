import argparse
from logger import setup_logger
from grid_trader import GridTrader
import ccxt

def main():
    parser = argparse.ArgumentParser(description='AI Grid Trading Script')
    args = parser.parse_args()

    logger = setup_logger()
    logger.info("Starting AI Grid Trading Script")

    exchange = ccxt.binance()  # Example exchange
    trader = GridTrader(exchange)
    trader.run()

if __name__ == '__main__':
    main()
