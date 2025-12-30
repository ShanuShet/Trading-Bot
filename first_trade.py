print("=== Script started ===")

from binance import Client
from config import API_KEY, API_SECRET

print("=== Creating client ===")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

print("=== Placing MARKET BUY order ===")

try:
    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )
    print("✅ ORDER PLACED SUCCESSFULLY")
    print(order)
except Exception as e:
    print("❌ ORDER FAILED:", e)

print("=== Script finished ===")
