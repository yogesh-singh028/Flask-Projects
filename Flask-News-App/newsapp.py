# create Virtual environment
# step 1 : pip3 install virtualenv
# step 2 : py -m venv virtual_env_name
# step 3 : .\virtual_env_name\Scripts\activate
# Step 4 : to deactivate use : deactivatepi
from flask import Flask, render_template
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
    return render_template('welcome.html',news_list=news_list)

if __name__ == "__main__":
    app.run(debug=True)
