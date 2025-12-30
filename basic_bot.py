from binance import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logging.basicConfig(
            filename="bot.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def set_margin_and_leverage(self, symbol, leverage):
        try:
            self.client.futures_change_margin_type(
                symbol=symbol,
                marginType="ISOLATED"
            )
        except Exception:
            pass

        self.client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(order)
            print("✅ Market order placed")
            return order
        except Exception as e:
            logging.error(e)
            print("❌ Error:", e)
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(order)
            print("✅ Limit order placed")
            return order
        except Exception as e:
            logging.error(e)
            print("❌ Error:", e)
            return None
