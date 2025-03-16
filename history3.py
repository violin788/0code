exec(open('util.py').read())
def his3(inp):
	"""
	import requests
	headers = {
	    'Content-Type': 'application/json'
	}
	#requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=5a8ead701dd5528066ea5229b4a6b2b1d24a0e02", headers=headers)
	requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/xom/prices?startDate=2021-1-1&endDate=2023-1-5", headers=headers)
	print(requestResponse.json())
	"""
	cwd = os.getcwd()
	fea =cwd+"\\ear" 
	fil = "xom"+".json"
	url = "https://api.tiingo.com/tiingo/daily/xom/prices?startDate=2021-1-1&endDate=2023-1-5"
	#req = requests.get(url)
	req = requests.get(url)
	data = req.json()
	print (data)
	sye()
	sav = fea+"\\"+fil
	with open(sav, 'w') as f:
	    json.dump(data, f)	
	#print (sto,a,lim)
	#print ("len miss = ",misn)




inp = []
his3(inp)