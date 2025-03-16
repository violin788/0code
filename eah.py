exec(open('util.py').read())
def eah(inp):
	cwd = os.getcwd()
	fea =cwd+"\\ear" 
	lis = os.listdir(fea)
	che = "dat.csv"
	if che not in lis:
		"""
		key = "FK98MBU38O64HAMH"
		url = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey='+key
		print(url)
		dat = requests.get(url)
		url_content = dat.content
		#change so that written into ear folder,not cod folder
		csv_file = open("dat.csv", 'wb')
		#change so that written into ear folder,not cod folder
		csv_file.write(url_content)
		csv_file.close()	
		"""
		naw = "naw"

	ray = []
	with open('dat.csv', newline='') as csvfile:
	    reader = csv.reader(csvfile)
	    for row in reader:
	    	ray.append(row)
	        #print(row)
	        #ray.append(row)
	pri(ray[0:100])
	#print(ray[0:100])





inp = []
eah(inp)