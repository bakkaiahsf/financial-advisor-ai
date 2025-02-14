import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from src.stock_data import get_stock_data
from src.news_analyzer import get_business_news, analyze_news_sentiment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Financial Advisor AI"}

@app.get("/stock/{stock_code}")
def fetch_stock(stock_code: str):
    return get_stock_data(stock_code)

@app.get("/news/")
def fetch_news():
    return get_business_news()

@app.get("/news/sentiment/")
def analyze_sentiment():
    news = get_business_news()
    return [{"headline": article["title"], "sentiment": analyze_news_sentiment(article["title"])} for article in news]