from binance import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

print("Placing LIMIT BUY order...")

order = client.futures_create_order(
    symbol="BTCUSDT",
    side="BUY",
    type="LIMIT",
    timeInForce="GTC",
    quantity=0.001,
    price=80000
)

print("✅ LIMIT ORDER PLACED")
print(order)
