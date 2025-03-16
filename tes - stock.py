exec(open('util.py').read())
def tes(inp):


	import yfinance as yf

	msft = yf.Ticker("TGT")

	hist = msft.history(period="5y")
	pri(hist)

	#opt = msft.option_chain('YYYY-MM-DD')
	#opt = msft.option_chain('2024-03-08')
	opt = msft.options
	print(opt)
	# get all stock info
	#print(msft.info)
	"""
	import yfinance as yf
	apple= yf.Ticker("aapl")
	# show actions (dividends, splits)
	apple.actions
	# show dividends
	apple.dividends
	# show splits
	apple.splits
	"""
	"""
	import yfinance as yf
	aapl = yf.Ticker("AAPL")
	data = aapl.info
	print(data)
	"""

inp = []
tes(inp)