exec(open('util.py').read())
def fin(inp):

	import finnhub
	finnhub_client = finnhub.Client(api_key="cd5d3iqad3i5nc8nt3s0cd5d3iqad3i5nc8nt3sg")

	print(finnhub_client.company_earnings('WBA', limit=5))

inp = []
fin(inp)