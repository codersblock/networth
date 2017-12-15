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
breakdown = {"ALT": 0};

for coin in distribution_hash:
    if coin == "USD":
        total_wealth_usd += float(distribution_hash[coin])
        breakdown["USD"] = float(distribution_hash[coin])
    else:
        coin_value = (float(pull_value(coin)) * float(distribution_hash[coin]))
        total_wealth_usd += coin_value
        if coin == "BTC":
            breakdown["BTC"] = coin_value
        elif coin == "ETH":
            breakdown["ETH"] = coin_value
        else:
            breakdown["ALT"] += coin_value


print ("Net Worth: $" + str(total_wealth_usd));
for coin in breakdown:
    percentage = breakdown[coin] / total_wealth_usd * 100.0
    print("  " + coin + ": " + str(breakdown[coin]) + " (" + str(percentage) + "%)")
