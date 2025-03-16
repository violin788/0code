exec(open('util.py').read())
def nas(inp):

	cwd = os.getcwd()
	fol =cwd+"\\ear"
	nam = "nas2"
	ext = "json"
	ext3 = "csv"
	fil = nam+"."+ext
	fil2 = fol+"\\"+fil
	fil3 = fol+"\\"+nam+"."+ext3 
	#jsw([fil2,dat])
	
	import quandl
	import nasdaqdatalink
	key = "xmefpKkxybsUgCpGhtqX"
	#inf = quandl.get_table("ZACKS/ES", paginate=True,api_key=key) 
	#data = nasdaqdatalink.get("FRED/GDP")
	#data = nasdaqdatalink.bulkdownload("ZACKS/ES",api_key=key)
	#data = nasdaqdatalink.get_table("EOD")
	#data = nasdaqdatalink.get_table('ZACKS/ES',ticker='AAPL',api_key=key)
	#data = nasdaqdatalink.get_table('ZACKS/ES',api_key=key)
	#data = nasdaqdatalink.get_table('QUOTEMEDIA/PRICES', ticker='AAPL',api_key=key)
	#data = nasdaqdatalink.get_table('QUOTEMEDIA/PRICES',ticker='XOM',api_key=key)
	#df = pd.DataFrame(data)
	#data = nasdaqdatalink.get_table('ZACKS/EA', start_date="2022-12-30", end_date="2023-01-30",api_key=key)
	data = nasdaqdatalink.get_table('ZACKS/EA',api_key=key)	

	data = nasdaqdatalink.get_table("WIKI/PRICES",api_key=key)	

	#"WIKIP"
	#data = quandl.get("FRED/re", start_date="2011-01-01", end_date="2022-12-29")
	#data = quandl.get("WIKI/AAPL")
	#data = quandl.get("WIKI/AAPL")
	print(data)
	print(fil2)
	data.to_json(fil2)
	data.to_csv(fil3) 
	
inp = []
nas(inp)