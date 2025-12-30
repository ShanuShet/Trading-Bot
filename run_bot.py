import logging

from src.client import get_client
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("=== Binance Futures Testnet Bot ===")

client = get_client(testnet=True)

symbol = input("Symbol (BTCUSDT): ").upper()
order_type = input("Order type (MARKET / LIMIT / STOP): ").upper()
side = input("Side (BUY / SELL): ").upper()
quantity = float(input("Quantity: "))

if order_type == "MARKET":
    order = place_market_order(client, symbol, side, quantity)

elif order_type == "LIMIT":
    price = float(input("Limit price: "))
    order = place_limit_order(client, symbol, side, quantity, price)

elif order_type == "STOP":
    stop_price = float(input("Stop price: "))
    limit_price = float(input("Limit price: "))
    order = place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price)

else:
    print("❌ Invalid order type")
    order = None

print("Order response:", order)
