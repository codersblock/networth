This is a simple python script that pulls market data from coinmarketcap, and calculates the worth of your holdings based on a json file with your coin amounts.

Written in [Python](https://www.python.org/)

It uses the [Python Requests library](http://docs.python-requests.org/en/master/user/install/) to make the REST call.  Follow the link for installation instructions.

json format example:

`{
	"BTC": 1,
	"ETH": 5,
	"DASH": 2
}`

The key is a ticker symbol, and the value is the number of coins / tokens of that type in your wallet.  By default, the application looks in your home directory for a file named 'distributions.json', but it shouldn't be too hard to figure out where to change this in the code.  It also handles the special case 'USD', if you want to include your dollar holdings in the sum.

to run:

`python networth.py`

sample output:

`Net Worth: $5.00
	BTC: $2.00
	ETH: $2.00
	ALT: $1.00`

