exec(open('util.py').read())
def eod(inp):

	#from eod import EodHistoricalData
	import eod
	# create the instance of the SDK
	api_key = 'YOUR_API_KEY_GOES_HERE'
	client = EodHistoricalData(api_key)
	resp = client.get_prices_eod('AAPL.US', from_='2021-03-01')
	print (resp)
		
inp = []
eod(inp)