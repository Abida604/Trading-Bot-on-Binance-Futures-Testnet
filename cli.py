from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def create_order(self, **params):
        return self.client.futures_create_order(**params)