import re
from chalice import Chalice

app = Chalice(app_name='alpaca-project')

@app.route('/')
def index():
    return {'hello': 'goose'}

@app.route('/buy_stocks', methods = ['GET'])
def buy_stock():
    request = app.current_request
    message = request.json_body
    data = {
        'symbol': 'AAPL',
        'qty': 1,
        'side': 'buy',
        'type': 'market',
        'time_in_force': 'gtc'
    }

    return {
        'message': 'Purchased the list of stocks according to the webscraping process.',
        'webhook_message': data['symbol']
    }

