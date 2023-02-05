import requests
import json

local_currency = "USD";
local_symbol = '$'


api_key= '77cc6d82-7a82-4cae-83eb-634202429fcf'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'http://pro-api.coinmarketcap.com'


global_url = base_url +'/v1/cryptocurrency/listings/latest?convert=' + local_currency

request = requests.get(global_url, headers=headers)

results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

for currency in data:
    name = currency["name"]
    symbol = currency["symbol"]
    
    price = currency['quote'][local_currency]['price']
    percent_change_24h = currency["quote"][local_currency]['percent_change_24h']
    market_cap = currency['quote'][local_currency]['market_cap']
    
    #rounding data
    price = round(price, 2)
    percent_change_24h = round(percent_change_24h, 2)
    market_cap = round(market_cap, 2)
    
    #formatting data
    price_string = local_symbol + '{:,}'.format(price)
    percent_change_24h = local_symbol + '{:,}'.format(percent_change_24h)
    market_cap = local_symbol + '{:,}'.format(market_cap)
    
    #concatenate
    print_price = 'Price:' + price_string
    print_percent_change_24h = '24h Percent Change : ' + percent_change_24h
    print_market_Cap = 'Market cap: ' + market_cap;
    
    print(name , symbol , print_price, print_percent_change_24h, print_market_Cap)
    print()
    
    
    