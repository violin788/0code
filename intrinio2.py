from __future__ import print_function

exec(open('util.py').read())
	
def intrinio2(inp):

	#from __future__ import print_function
	import time
	import intrinio_sdk as intrinio
	from intrinio_sdk.rest import ApiException

	intrinio.ApiClient().set_api_key('OjA1ZDkxNjNkZGJlODZlZGFlM2UxZTA2NWM1Y2Q5ODBj')
	intrinio.ApiClient().allow_retries(True)

	identifier = "AAPL"
	start_date = "2018-01-01"
	end_date = "2019-01-01"
	frequency = 'daily'
	page_size = 10
	next_page = "~null"

	response = intrinio.SecurityApi().get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, page_size=page_size, next_page=next_page)
	print(response)	
	
inp = []
intrinio2(inp)