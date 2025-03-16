exec(open('util.py').read())
def peh(inp):
	
	import requests

	url = "https://pe-history.p.rapidapi.com/stock/"

	querystring = {"ticker":"AAPL","begin_date":"2021-01-01","end_date":"2022-07-01"}

	headers = {
		"X-RapidAPI-Key": "d3d4233d48msh7591fc9e1fc7125p1aa094jsn631153bc8cf2",
		"X-RapidAPI-Host": "pe-history.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)

inp = []
peh(inp)