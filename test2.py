import requests 
news_api = "0e049d48893441a98f3352b0ca87fefd"
def get_news():
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"

    response = requests.get(url)
    data = response.json()

    return data

news = get_news()
print(news)
