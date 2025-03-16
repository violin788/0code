exec(open('util.py').read())
from tkinter import *
def deriv2(inp):
	import requests
	import numpy as np
	from datetime import datetime
	trading_data = inp
	symbol = trading_data[0]
	date_in_question = trading_data[1]
	call_or_put = trading_data[2]
	override_expiration = trading_data[3]
	"""
	#old input method
	# if len override_price>0, then price overrides
	trading_data = trading_inputs([])
	symbol = trading_data[0]
	date_in_question = trading_data[1]
	call_or_put = trading_data[2]
	override_expiration = trading_data[3]
	#date_in_question = "2024-03-08"
	#call_or_put = "c"
	#override_expiration = "515"
	"""
	#date_in_question = "2023-11-29"
	#dat2 = datetime.datetime.strptime(dat,'%b %d, %Y')
	from datetime import datetime
	date_object = datetime.strptime(date_in_question,'%Y-%m-%d')
	day_of_week = date_object.weekday()
	if day_of_week==4:
		#next_friday = date_in_question
		next_friday = datetime.strptime(date_in_question,'%Y-%m-%d')
	if day_of_week!=4:
		import datetime
		if day_of_week<4:
			next_friday = date_object+datetime.timedelta(4-day_of_week)
		if day_of_week>4:
			next_friday =date_object+datetime.timedelta(11-day_of_week) 
	print(date_in_question)
	print(day_of_week)
	print(next_friday)
	if len(symbol)==0:
		symbol =str(input("symbol = "))
	move_week = 0
	#if len(date_of_options)==0:
	#	move_week = int(str(input("move week = ")))
	#override_price = "20"
	if len(override_expiration)==0:
		override_expiration =str(input("override_price = "))
	symbol = symbol.upper()
	call_or_put = call_or_put.upper()
	price = override_expiration
	#symbol = "AMD"
	#override_price = "20"
	#symbol = "SPY"
	#start_date = "2024-01-26"
	#start_date = "2024-02-01"
	#start_date = "2024-02-08"
	#start_date = "2024-02-16"
	#start_date = "2024-02-23"
	#start_date = "2024-03-01"
	#start_date = "2024-03-08"
	start_date = date_in_question
	from datetime import datetime
	start_date_object = datetime.strptime(start_date,'%Y-%m-%d')
	#start_date_object = start_date
	import datetime
	start_date_delta = start_date_object-datetime.timedelta(7*move_week)
	start_date_converted = start_date_delta.strftime('%Y-%m-%d')
	print(start_date_converted)
	start_date = start_date_converted
	#sye()
	from datetime import datetime
	#sye()
	end_date = start_date_converted
	#end_date = "2024-02-23"
	folder = os.getcwd()
	earn_folder = folder+"\\earn\\"
	earn_list = os.listdir(earn_folder)
	file_name = symbol+"."+start_date+".json"
	save_file = earn_folder+file_name
	#print(file_name)
	#sye()
	if file_name not in earn_list:
		#get stock prices
		url1 = "https://api.polygon.io/v2/aggs/ticker/"
		url2 = "/range/1/minute/"
		url3 = "/"
		url4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
		url = url1+symbol+url2+start_date+url3+end_date+url4
		#getting data from polygon with json
		polygon_check([])
		data_back = requests.get(url)
		json_data = data_back.json()
		#print("-----------------have done request to polygon--------------------")
		with open(save_file, 'w') as f:
		    json.dump(json_data, f)
		wri2([save_file,json_data])
		print("output file = ",save_file)
		print("have gotten stock data..")
		sle([5])
	price_info = load_data([save_file])
	#print("save file",save_file)
	minute_data = price_info["results"]
	if len(str(price))==0:
		price = minute_data[4]["c"]
	print ("price = ",price)
	#if len(str(price))==0:
	#	price = float(override_price)	
	price2 = round(float(price))
	options_code = str(price2)+"000"
	for a in range(0,8-len(options_code)):
		options_code = "0"+options_code
	options_code =call_or_put+options_code
	#file_name = symbol+"."+start_date+"."+options_code+".json"
	#save_file = earn_folder+file_name
	print(file_name)
	url_options1 = "https://api.polygon.io/v2/aggs/ticker/O:"
	#start_date_object = datetime.strptime(start_date,'%Y-%m-%d')
	expiration_year = next_friday.strftime("%y")
	expiration_month = next_friday.strftime("%m")
	expiration_day = next_friday.strftime("%d")
	options_date = expiration_year+expiration_month+expiration_day
	options_code = options_date+options_code
	url_options2 = "/range/1/minute/"
	url_options3 = "/"
	url_options4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
	url_options = url_options1+symbol+options_code+url_options2+start_date+url_options3+end_date+url_options4
	#getting data from polygon with json
	print(url_options)
	print(options_code)
	file_name = symbol+"."+start_date+"."+options_code+".json"
	save_file = earn_folder+file_name
	print(file_name)
	print(save_file)
	#sye()
	if file_name not in earn_list:
		polygon_check([])
		data_back = requests.get(url_options)
		json_data = data_back.json()
		#print("-----------------have done request to polygon--------------------")
		with open(save_file, 'w') as f:
		    json.dump(json_data, f)
		print("output file = ",save_file)
		print("now gotten options data..")
	data_dictionary = load_data([save_file])
	#pri(data_dictionary['results'])
	options_data = []
	skip_early = 0
	for a,val in enumerate(data_dictionary['results']):
		more = []
		timestamp_integer = int(val["t"])
		timestamp_integer = (timestamp_integer)/1000
		timestamp_object = datetime.fromtimestamp(timestamp_integer)
		converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
		if "09:30" in converted_time:
			skip_early = 1
		#if skip_early==0:
		#	continue
		more.append(converted_time)
		more.append(val["o"])
		more.append(val["h"])
		more.append(val["l"])
		more.append(val["c"])
		options_data.append(more)
		if "16:00" in converted_time:
			break
	pri(options_data)
	import pandas as pd
	dataframe = pd.DataFrame(options_data)
	#print(dataframe)
	import plotly.graph_objects as go
	from datetime import datetime
	#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
	print(file_name)
	print(dataframe)
	#sye()
	fig = go.Figure(data=[go.Candlestick(x=dataframe[0],
					open=dataframe[1],
	                high=dataframe[2],
	                low=dataframe[3],
	                close=dataframe[4])])
	fig.update_layout(
    title=file_name
    )
	fig.show()

#interface used to run it..
import tkinter
import tkinter as tk
master = Tk()
master.title("GUI")
master.geometry("200x120")
Label(master, text='Symbol').grid(row=0)
Label(master, text='Date in Question').grid(row=1)
Label(master, text='Call or Put').grid(row=2)
Label(master, text='Override Expiration').grid(row=3)
Label(master, text='Get info').grid(row=4)
e1 = Entry(master)
e1.insert(END,"SPY") 
e2 = Entry(master)
e2.insert(END,"2024-03-07")
e3 = Entry(master)
e3.insert(END,"p")
e4 = Entry(master)
e4.insert(END,"510")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
def run_whole_thing():
	#symbol = e1
	#print(symbol)
	symbol = e1.get()
	date_in_question = e2.get()
	call_or_put = e3.get()
	override_expiration = e4.get()
	inputs = [symbol,date_in_question,call_or_put,override_expiration]
	deriv2(inputs)
B = Button(master, text ="Get info", command = run_whole_thing)
B.place(x=110,y=85)
print(e1,e2)
mainloop()

#inp = []
#deriv2(inp)