from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

print("KEY CHECK:", API_KEY)
print("SECRET CHECK:", API_SECRET)

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com"

account = client.futures_account()
print("\n✅ ACCOUNT CONNECTED SUCCESSFULLY")
print(account)