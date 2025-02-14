import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(stock_code):
    """Fetch latest stock data from Alpha Vantage API"""
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock_code,
        "interval": "5min",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch stock data"}

# Example Usage
if __name__ == "__main__":
    print(get_stock_data("TCS.BSE"))
