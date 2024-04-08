import requests
import json

url = 'https://api.coingecko.com/api/v3/simple/price'
params = {  
        'ids': 'ethereum,bitcoin,shiba-inu,litecoin',
        'vs_currencies': 'usd',
}

response = requests.get(url, params = params)

if response.status_code == 200:
        print('Data retrieved successfully')
        data = response.json()
        with open('coingecko/cryptocurrency_prices.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
else:
        print('Failed to retrieve data from the API')