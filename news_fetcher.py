import requests

API_KEY = "ca77e94226244119b55ac49009983ae6"

def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = []
        for article in data['articles']:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'urlToImage': article['urlToImage'] or 'https://via.placeholder.com/300x180'
            })
        return articles
    else:
        return []
