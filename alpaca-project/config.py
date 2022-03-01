API_KEY = 'PK098PEZ5L9GSA4L1CB0'
SECRET_KEY = 'vwfSV5OOJR24ZMYbHNYSKG3kWpV5F33o3ZCvW6Ss'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

HEADERS = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': SECRET_KEY
}

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)
