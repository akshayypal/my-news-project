from flask import Flask, render_template, request
from news_fetcher import get_news  # Your news fetching function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Load the homepage

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']  # Get the keyword from the form
    news_articles = get_news(keyword)  # Fetch news articles using your function
    
    # Ensure articles is a list of dictionaries with keys: 'title', 'description', 'url', and 'urlToImage'
    return render_template('results.html', articles=news_articles)

if __name__ == '__main__':
    app.run()


