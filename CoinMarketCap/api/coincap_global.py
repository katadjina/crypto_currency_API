import requests
import json

local_currency = "USD";
local_symbol = '$'


api_key= '77cc6d82-7a82-4cae-83eb-634202429fcf'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'http://pro-api.coinmarketcap.com'

#in order to factor this in (local currency) we have to pass our first parameter into the constructor
# the url
global_url = base_url +'/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(global_url, headers=headers)

results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

btc_dominance = data["btc_dominance"];
eth_dominance = data["eth_dominance"];


total_market_cap = data["quote"][local_currency]["total_market_cap"]
total_volume_24h = data["quote"][local_currency]["total_volume_24h"]
#print(total_volume_24h);

total_market_cap = round(total_market_cap, 2)
total_volume_24h = round(total_volume_24h, 2)
btc_dominance = round(btc_dominance, 2)
eth_dominance = round(eth_dominance, 2)

total_market_cap_string = local_symbol + '{:,}'.format(total_market_cap)
total_volume_24h_string = local_symbol + '{:,}'.format(total_volume_24h)


print(total_market_cap_string)
print(total_volume_24h_string)