import requests
from bs4 import BeautifulSoup
import config

oversold_url = 'https://finviz.com/screener.ashx?v=111&s=ta_oversold&f=exch_nasd'
overbought_url = 'https://finviz.com/screener.ashx?v=111&s=ta_overbought&f=exch_nasd'

def get_stock(url=oversold_url): # gets oversold URL by default; can also switch to overbought_url
    headers = {'User-Agent': config.USER_AGENT}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('a', {'class': 'screener-link-primary'})
    return [row.text for row in rows]

