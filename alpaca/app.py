from chalice import Chalice
# import requests
# from bs4 import BeautifulSoup

app = Chalice(app_name='alpaca')

@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/oversold')
def get_stock(): # gets oversold URL by default; can also switch to overbought_url

    API_KEY = 'Your API-KEY Here'
    SECRET_KEY = 'Your SECRET-KEY Here'
    USER_AGENT = 'Your User-Agent Here'
    HEADERS = {
        'APCA-API-KEY-ID': API_KEY,
        'APCA-API-SECRET-KEY': SECRET_KEY
    }

    BASE_URL = 'https://paper-api.alpaca.markets'
    ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
    ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
    POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)

    oversold_url = 'https://finviz.com/screener.ashx?v=111&s=ta_oversold&f=exch_nasd'
    headers = {'User-Agent': USER_AGENT}
    r = requests.get(oversold_url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('a', {'class': 'screener-link-primary'})
    return [row.text for row in rows]
