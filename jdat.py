exec(open('util.py').read())
def jdat():

	import json

	# Open and load the JSON file
	with open('earnings_data.json', 'r') as file:
	    data = json.load(file)

	# Now `data` contains the content of the JSON file
	data2 = data["earningsCalendar"]
	counter = 0
	values = []
	for a,val in enumerate(data2):
		#print(a,val)
		symbol = val["symbol"]
		date = val["date"]
		hour = val["hour"]
		if len(hour)==0:
			continue
		counter = counter+1
		new = [date,symbol,hour]
		print(new)
		values.append(new)
	values.reverse()
	for a,val in enumerate(values):
		print(a,val)
	
jdat()