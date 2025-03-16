
exec(open('util.py').read())
def compare(inp):	

	import yfinance as yf
	folder = os.getcwd()
	earn_folder = folder+"\\earn"
	symbol = "amzn"
	print(symbol)
	file_extension = ".csv"	
	symbol = symbol.upper()
	check = symbol+"-yfinance_history"+file_extension
	earn_list = os.listdir(earn_folder)
	check_file = earn_folder+"\\"+check
	if check not in earn_list:
		yfinance_information = yf.Ticker(symbol)
		price_history_5y = yfinance_information.history(period="5y")
		price_history_5y = price_history_5y[::-1]
		wri2([check_file,price_history_5y])
	price_history = load_data([check_file])
	price_history = price_history[0:255]
	for a,val in enumerate(price_history):
		for b,valb in enumerate(val):
			if b==0:
				continue
			price_history[a][b] = decimal_places([valb,2])
	pri(price_history)
	new_list = []
	for a,val in enumerate(price_history):
		date = val[0]
		high = val[2]
		low = val[3]
		val[0] = date[0:date.find(" ")]
		try:
			difference = float(high)-float(low)
		except:
			continue
		difference = decimal_places([difference,2])
		percent = (float(difference)/float(high))*100
		percent = decimal_places([percent,2])
		#val = val[0:5]
		more = [percent,difference]+val[0:6]
		new_list.append(more)
	new_list.sort(key=lambda x:x[0],reverse=True)
	new_list = new_list[0:20]
	pri(new_list)


inp = []
compare(inp)