import os

os.environ["API_KEY"] = "your_key"
os.environ["API_SECRET"] = "your_secret"

print(os.getenv("API_KEY"))
print(os.getenv("API_SECRET"))