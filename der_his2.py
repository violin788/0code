exec(open('util.py').read())
def der_his2(inp):
	import requests
	import numpy as np
	from datetime import datetime
	symbol = "NVDA"
	start_date = "2024-02-23"
	end_date = "2024-02-23"
	url1 = "https://api.polygon.io/v2/aggs/ticker/"
	url2 = "/range/1/minute/"
	url3 = "/"
	url4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
	url = url1+symbol+url2+start_date+url3+end_date+url4
	folder = os.getcwd()
	earn_folder = folder+"\\earn\\"
	earn_list = os.listdir(earn_folder)
	save_file = earn_folder+symbol+"."+start_date+".json"
	data_dictionary = load_data([save_file])
	new_list =dictionary_to_list3([data_dictionary])
	pri(new_list[0])
	print(new_list[5])
	for a,val in enumerate(new_list[5]):
		print(a,val)
	minute_prices_header = []
	minute_prices_header.append("Time")
	minute_prices_header.append("Open")
	minute_prices_header.append("Close")
	minute_prices_header.append("High")
	minute_prices_header.append("Low")
	minute_prices = [minute_prices_header]
	pri(minute_prices)
	for a,val in enumerate(new_list[5]):
		timestamp_integer = int(val[7])
		timestamp_integer = (timestamp_integer+18000000)/1000
		timestamp_object = datetime.fromtimestamp(timestamp_integer)
		converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
		price_open = decimal_places([val[3],2])
		price_close = decimal_places([val[4],2])
		price_high = decimal_places([val[5],2])
		price_low = decimal_places([val[6],2])
		more = [converted_time,price_open,price_close,price_high,price_low]
		minute_prices.append(more)
		if "16:30" in converted_time:
			break
	pri(minute_prices)
	#lst = ['fav', 'tutor', 'coding', 'skills']
	import pandas as pd
	dataframe = pd.DataFrame(minute_prices)
	print(dataframe)
	import matplotlib.pyplot as plt
	from mplfinance import candlestick_ohlc
	import pandas as pd
	import matplotlib.dates as mpdates
	#plt.style.use('dark_background')
	fig, ax = plt.subplots()
	candlestick_ohlc(ax, dataframe.values, width = 0.6,
                 colorup = 'green', colordown = 'red', 
                 alpha = 0.8)
	plt.show()
 
	"""
	#getting data from polygon with json
	data_back = requests.get(url)
	json_data = data_back.json()
	with open(output_file, 'w') as f:
	    json.dump(json_data, f)
	wri2([output_file,json_data])
	sw2([output_file,1])
	print(json_data)
	"""
inp = []
der_his2(inp)