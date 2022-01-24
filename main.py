import config
import scrape
import requests, json

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

def buy_oversold():
    oversold = scrape.get_stock(scrape.oversold_url)
    bought = [create_order(symbol) for symbol in oversold]

    for stock in bought:
        print('Stock ' + stock['symbol'] + ' was bought.')

buy_oversold()