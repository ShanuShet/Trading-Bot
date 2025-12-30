from binance import Client
from config import API_KEY, API_SECRET

def get_client(testnet=True):
    client = Client(API_KEY, API_SECRET)

    if testnet:
        client.FUTURES_URL = "https://testnet.binancefuture.com"

    return client
