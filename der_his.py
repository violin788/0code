exec(open('util.py').read())
def der_his(inp):
	from datetime import date
	import yfinance as yf
	stock = "AAPL"
	today = date.today()
	day_of_week = today.weekday()
	next_friday = ""
	if day_of_week<4:
		change = 4-day_of_week
	if day_of_week>=4:
		change = 11-day_of_week
	next_friday = today+datetime.timedelta(change)
	print(today,day_of_week)
	print(next_friday)
	stock_info = yf.Ticker(stock)
	print(stock_info)
	print(stock_info.options)
	sye()
	options_data = stock_info.option_chain(next_friday)
	put_options = options_data.puts
	call_options = options_data.calls 
	pri(put_options)
	pri(call_options)
	sye()


	"""
	except:
		print ("waiting to requery for new friday..")
		sle([5])
		#cha = yf.Ticker(stock)
		aga = "2023-04-21"
		opt = cha.option_chain(aga)
		"""
	put = opt.puts
	cal = opt.calls 
	#print (type(opt))
	#print(put,cal)
	put.to_csv(fip)
	cal.to_csv(fic)
	get = 1
		
	
inp = []
der_his(inp)