from chalice import Chalice
import config
import requests
from bs4 import BeautifulSoup

app = Chalice(app_name='alpaca')

@app.route('/')
def index():
    return {'hello': config.BASE_URL}

@app.route('/buy_stock', methods = ['POST'])
def buy_stock():
    return {'api_key': 'Your API Key here'}

@app.route('/oversold')
def get_stock(): # gets oversold URL by default; can also switch to overbought_url

    oversold_url = 'https://finviz.com/screener.ashx?v=111&s=ta_oversold&f=exch_nasd'
    headers = {'User-Agent': config.USER_AGENT}
    r = requests.get(oversold_url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('a', {'class': 'screener-link-primary'})
    return [row.text for row in rows]

