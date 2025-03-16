exec(open('util.py').read())
def his(inp):
		
	import requests

	url = "https://stock-analysis.p.rapidapi.com/api/v1/resources/earnings-history"

	querystring = {"ticker":"AAPL"}

	headers = {
		"X-RapidAPI-Key": "d3d4233d48msh7591fc9e1fc7125p1aa094jsn631153bc8cf2",
		"X-RapidAPI-Host": "stock-analysis.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)	
	
inp = []
his(inp)