
from basic_bot import BasicBot
from config import API_KEY, API_SECRET

print("=== Creating bot ===")

bot = BasicBot(API_KEY, API_SECRET, testnet=True)

print("=== Bot created successfully ===")

symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
leverage = int(input("Enter leverage (e.g. 10): "))

bot.set_margin_and_leverage(symbol, leverage)

order_type = input("Order type (MARKET / LIMIT): ").upper()
side = input("Side (BUY / SELL): ").upper()
quantity = float(input("Quantity: "))

if order_type == "MARKET":
    order = bot.place_market_order(symbol, side, quantity)
elif order_type == "LIMIT":
    price = float(input("Limit price: "))
    order = bot.place_limit_order(symbol, side, quantity, price)
else:
    print("Invalid order type")
    order = None

print("Order response:", order)

