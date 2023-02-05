import os 
import csv #for readinf csv format
import json
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style


local_currency = "USD";
local_symbol = '$'


api_key= '77cc6d82-7a82-4cae-83eb-634202429fcf'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'http://pro-api.coinmarketcap.com'


print()
print("MY PORTFOLIO")
print()

portfolio_value = 0.00

table = PrettyTable(['Asset', 'Amount Owned', 'Value' , 'Price' , '1h' , '24h' , '7d'])

#open csv file:

my_file_path = '/Users/katq/Desktop/CoinMarketCap/projects/project1/my_portfolio.csv'

with open(my_file_path , "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        #looking for hidden character in the file --> only for mac!
        if '\ufeff' in line[0]:
            line[0] = line[0][1:].upper()
        else:
            line[0] = line[0].upper()
          
        symbol = line[0]    
        amount = line[1]
        
        quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol
        
        request = requests.get(quote_url, headers=headers)
        results = request.json()
        
        #print(json.dumps(results, sort_keys=True, indent=4))
        
        currency = results['data'][symbol]
        
        name = currency['name']
        
        quote = currency['quote'][local_currency]
        
        hour_change = round(quote['percent_change_1h'], 1)
        day_change = round(quote['percent_change_24h'], 1)
        week_change = round(quote['percent_change_7d'], 1)     
        
        price = quote['price']
        value = float(price)  * float(amount)  
        
        
        portfolio_value += value;
        
        #coloring the tables
        
        
        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' +  Style.RESET_ALL    
        
        if day_change > 0:
                hour_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' +  Style.RESET_ALL  
              
        
        if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' +  Style.RESET_ALL    
            

        
        
        
        price_string = '{:,}'.format(round(price,2))
        value_string = '{:,}'.format(round(value,2))
        
        table.add_row([name + '(' + symbol + ')',
                      amount,
                      local_symbol + value_string,
                      local_symbol + price_string,
                      str(hour_change),
                      str(day_change),
                      str(week_change)])

print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value, 2))
print('Total Portfolio Value: ' + Back.GREEN + local_symbol + portfolio_value_string  + Style.RESET_ALL)
        