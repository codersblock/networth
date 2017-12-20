import json
import requests
import os

ticker = requests.get("https://api.coinmarketcap.com/v1/ticker/").json()

ticker_hash = {}
for coin in ticker:
    ticker_hash[coin['symbol']] = coin

def pull_value(coin):
    return ticker_hash[coin]["price_usd"]

f = open(os.environ["HOME"] + "/distributions.json", "r")
distribution_hash = json.load(f);

total_wealth_usd = 0.0;
breakdown = {};

for coin in distribution_hash:
    if coin == "USD":
        total_wealth_usd += float(distribution_hash[coin])
        breakdown["USD"] = float(distribution_hash[coin])
    else:
        coin_value = (float(pull_value(coin)) * float(distribution_hash[coin]))
        total_wealth_usd += coin_value
        breakdown[coin] = coin_value

print ("Net Worth: $" + str(total_wealth_usd));

sorted_by_percentage = [];
percentages = {};

for coin in breakdown:
    percentage = breakdown[coin] / total_wealth_usd * 100.0
    percentages[coin] = percentage;

    loop = 0;
    while (loop < len(sorted_by_percentage) and percentages[sorted_by_percentage[loop]] > percentage):
        loop += 1;

    sorted_by_percentage.insert(loop, coin);
            
for coin in sorted_by_percentage:
    print("  " + coin + ": $" + str(round(breakdown[coin], 2)) + " (" + str(round(percentages[coin], 2)) + "%)")
