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
