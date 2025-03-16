exec(open('util.py').read())
def rap(inp):

	import requests

	url = "https://alpha-vantage.p.rapidapi.com/query"

	querystring = {"symbol":"MSFT","function":"TIME_SERIES_INTRADAY","interval":"5min","output_size":"compact","datatype":"json"}

	headers = {
		"X-RapidAPI-Key": "d3d4233d48msh7591fc9e1fc7125p1aa094jsn631153bc8cf2",
		"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)

inp = []
rap(inp)