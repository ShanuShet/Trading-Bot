print("=== Script started ===")

from binance import Client

API_KEY = "PASTE_YOUR_TESTNET_API_KEY"
API_SECRET = "PASTE_YOUR_TESTNET_SECRET"

print("=== Creating client ===")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

print("=== Fetching balance ===")

try:
    balance = client.futures_account_balance()
    print("✅ API CONNECTED SUCCESSFULLY")
    for asset in balance:
        if asset["asset"] == "USDT":
            print("USDT Balance:", asset["balance"])
except Exception as e:
    print("❌ ERROR:", e)

print("=== Script finished ===")
