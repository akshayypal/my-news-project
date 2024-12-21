import requests

#Arbaz's project
api_key = "ca77e94226244119b55ac49009983ae6"

def get_news(query):  
    # NewsAPI URL
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Parse the response into JSON
        
        # Check if there are articles
        if data['totalResults'] > 0:
            print(f"\nTop news articles for '{query}':")
            # Loop through the articles and display their titles and descriptions
            for article in data['articles']:
                title = article['title']
                description = article['description']
                url = article['url']
                
                # Display the article's title, description, and URL
                print(f"\nTitle: {title}")
                print(f"Description: {description}")
                print(f"Read more: {url}")
        else:
            print(f"No articles found for '{query}'")
    else:
        print(f"Failed to fetch news. Error code: {response.status_code}")

# Input from the user
query = input("Enter a topic or keyword to search news: ")
get_news(query)
