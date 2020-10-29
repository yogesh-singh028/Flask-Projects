from flask import Flask, render_template, request, redirect, url_for
from urllib.request import urlopen
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://news.google.com/news/rss'
    client = urlopen(url)
    xml_data = client.read()
    client.close()
    soup = BeautifulSoup(xml_data,'xml')
    print(soup.title)
    news_list = soup.find_all('item')
    
    return render_template('news.html',news_list=news_list)

    

if __name__ == "__main__":
    app.run(debug=True)
