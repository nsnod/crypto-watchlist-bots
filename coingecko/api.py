import requests
url = 'https://api.coingecko.com/api/v3/simple/price'
params = {  
        'ids': 'ethereum,bitcoin',
        'vs_currencies': 'usd',
}

response = requests.get(url, params = params)

if response.status_code == 200:
        data = response.json()
        Ethereum_price = data['ethereum']['usd']
        bitcoin_price = data['bitcoin']['usd']
        print(f'The price of Bitcoin in USD is ${bitcoin_price}')
        print(f'The price of Ethereum in USD is ${Ethereum_price}')
else:
        print('Failed to retrieve data from the API')
