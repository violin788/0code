exec(open('util.py').read())
def deriv(inp):

	import requests
	import numpy as np
	from datetime import datetime
	# if len override_price>0, then price overrides
	trading_data = trading_inputs([])
	symbol = trading_data[0]
	date_in_question = trading_data[1]
	#symbol = "spy"
	#date_in_question = "2024-03-01s"
	#date_in_question = "2024-02-23"
	#date_in_question = "2024-03-01"
	#date_in_question = "2024-03-08"
	end_prices= date_in_question
	symbol = symbol.upper()
	
	#start_date = "2023-11-29"
	#end_date = start_date
	#end_date = "2024-02-23"
	folder = os.getcwd()
	earn_folder = folder+"\\earn\\"
	earn_list = os.listdir(earn_folder)
	file_name = symbol+"."+date_in_question+".json"
	save_file = earn_folder+file_name
	print(file_name)
	#sye()
	if file_name not in earn_list:
		url1 = "https://api.polygon.io/v2/aggs/ticker/"
		url2 = "/range/1/minute/"
		url3 = "/"
		url4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
		url = url1+symbol+url2+date_in_question+url3+end_prices+url4
		#getting data from polygon with json
		data_back = requests.get(url)
		json_data = data_back.json()
		with open(save_file, 'w') as f:
		    json.dump(json_data, f)
		wri2([save_file,json_data])
		#sw2([save_file,1])
		print(json_data)
	price_info = load_data([save_file])
	#print("save file",save_file)
	minute_data = price_info["results"]
	pri(minute_data)
	skip_early = 0
	converted = []
	#skip = 0
	for a,val in enumerate(minute_data):
		#print(a,val)
		#print(val["t"])
		timestamp_integer = int(val["t"])
		#adjust for greenwich mean time?
		timestamp_integer = (timestamp_integer)/1000
		timestamp_object = datetime.fromtimestamp(timestamp_integer)
		#converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
		converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
		if "09:30" in converted_time:
			skip_early=1
		if skip_early<1:
			continue
		print(converted_time)
		#minute_data[val]['t'] = converted_time
		more = [converted_time,val["o"],val["h"],val["l"],val["c"]]
		"""
		if skip==1:
			skip = 0
			continue
		if skip==0:
		"""
		converted.append(more)
		#skip = 1
		
		#more.append()
		#val["t"] = converted_time
		if "16:00" in converted_time:
			break
	pri(converted)
	dataframe = pd.DataFrame(converted)
	print(dataframe)	
	import plotly.graph_objects as go
	from datetime import datetime
	#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
	print(file_name)
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


	
inp = []
deriv(inp)