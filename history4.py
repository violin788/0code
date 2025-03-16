exec(open('util.py').read())
def his4(inp):
	"""
	from yahoofinance import HistoricalPrices
	req = HistoricalPrices('AAPL')
	print(req)
	"""

	import yfinance as yf
	msft = yf.Ticker("XOM")
	#hist = msft.history(period="max")
	hist = msft.history(period="5y")
	#dat = msft.quarterly_earnings(period="max")
	#hist.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')
	hist.to_csv('naw.csv')
	hist.to_json('naw.json')

	print(hist)
	#print(dat)
	
inp = []
his4(inp)