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
	"""
	finnhub_client = finnhub.Client(api_key="cd5d3iqad3i5nc8nt3s0cd5d3iqad3i5nc8nt3sg")
	dat = finnhub_client.earnings_calendar(_from="2023-01-01", to="2023-01-30", symbol="", international=False)
	with open("fin.json","w") as outfile:
		json.dump(dat,outfile)
	print(dat)
	"""
	inf = js2([fil])
	print(inf)
	sye()
	inf2 = inf["earningsCalendar"]#[0]
	tak = []
	ski = ["2022","08","09","10","11","12","13","14","15"]
	for a,val in enumerate(inf2):
		app = []
		rev = val["revenueEstimate"]
		if "None" in str(rev):
			rev = 0
		app.append(rev)
		app.append(val["symbol"])
		day = val["date"]
		ove = 0
		for b,val2 in enumerate(ski):
			if val2 in day:
				ove = 1
		if ove==1:
			continue
		app.append(val["date"])

		tak.append(app)

	tak.sort(reverse=True)
	pri(tak)
		#print (val)

	#print(len(inf2))
	#sye()
	#inf2 = str(inf)[0:100]
	#inf2 = inf[0]
	#["earningsCalendar"]
	#for a,val in enumerate(inf):
		#print(val)
	#print(inf2)


inp = []
fin2(inp)