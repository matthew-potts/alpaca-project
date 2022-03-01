import requests
from bs4 import BeautifulSoup
import config
import json

oversold_url = 'https://finviz.com/screener.ashx?v=111&s=ta_oversold&f=exch_nasd'
overbought_url = 'https://finviz.com/screener.ashx?v=111&s=ta_overbought&f=exch_nasd'
user_headers = {'User-Agent': config.USER_AGENT}

def get_stock(url=oversold_url): # gets oversold URL by default; can also switch to overbought_url
    r = requests.get(url, headers = user_headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('a', {'class': 'screener-link-primary'})
    return [row.text for row in rows]

def create_order(symbol, qty = 1, side = 'buy', type = 'market', time_in_force = 'day'):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(config.ORDERS_URL, json = data, headers = config.HEADERS)
    return json.loads(r.content)

def get_orders():
    r = requests.get(config.ORDERS_URL, headers = config.HEADERS)
    return json.loads(r.content)

def get_positions():
    r = requests.get(config.POSITIONS_URL, headers = config.HEADERS)
    ls = []
    ls.append({i['symbol']: [i['market_value'], i['unrealized_pl']] for i in json.loads(r.content)})
    return ls

def buy_oversold():
    oversold = get_stock()
    bought = [create_order(symbol) for symbol in oversold]
    ls = []
    for i in bought:
        try:
            ls.append(i['symbol'])
        except KeyError:
            pass
    return [f'Stock {i} was bought' for i in ls] # add a price to this!
print(buy_oversold())