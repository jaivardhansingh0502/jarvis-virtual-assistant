import requests 
import os
from dotenv import load_dotenv

load_dotenv()

news_api = os.getenv("NEWS_API_KEY")
def get_news():
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"

    response = requests.get(url)
    data = response.json()

    return data

news = get_news()
print(news)
