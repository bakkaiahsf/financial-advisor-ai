import requests
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def get_business_news(query="stock market"):
    """Fetch latest business news from Google News API"""
    params = {
        "q": query,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()["articles"][:5]  # Get top 5 news articles
    else:
        return {"error": "Unable to fetch news"}

# Sentiment Analysis
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_news_sentiment(news):
    """Analyze sentiment of news headlines"""
    return sentiment_pipeline(news)

# Example Usage
if __name__ == "__main__":
    news = get_business_news()
    for article in news:
        sentiment = analyze_news_sentiment(article["title"])
        print(f"Headline: {article['title']}")
        print(f"Sentiment: {sentiment}")