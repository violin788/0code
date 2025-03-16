exec(open('util.py').read())
def fin2(inp): 
	import finnhub
	cwd = os.getcwd()
	fol =cwd+"\\ear"
	nam = "fin"
	ext = "json"
	fil = nam+"."+ext
	fil2 = fol+"\\"+fil
	print(fil2)
	#sye()
	#print("naw")

	finnhub_client = finnhub.Client(api_key="cd5d3iqad3i5nc8nt3s0cd5d3iqad3i5nc8nt3sg")
	dat = finnhub_client.earnings_calendar(_from="2022-12-15", to="2023-01-15", symbol="", international=False)

	with open("fin.json","w") as outfile:
		json.dump(dat,outfile)

	print(dat)
	#json_object = json.dumps(dictionary, indent = 4)
	#jsw = json.dumps(dat) 
	#print(jsw)


	#sprint(dat)		

	#print(finnhub_client.earnings_calendar(_from="2022-12-15", to="2023-01-15", symbol="", international=False))

inp = []
fin2(inp)