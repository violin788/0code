exec(open('util.py').read())
def fln2(inp):
	was = []
	was.append(["arn","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	was.append(["got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	was.append(["osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	was.append(["cph","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	was.append(["ber","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNCRVJwAYIBCwj___________8BQAFIAZgBAg"])
	was.append(["fra","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNGUkFwAYIBCwj___________8BQAFIAZgBAg"])
	was.append(["par","https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNXF0anABggELCP___________wFAAUgBmAEC"])
	was.append(["lon","https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNGpwbHABggELCP___________wFAAUgBmAEC"])
	for a,val in enumerate(was):
		was[a].insert(0,"was")

	nyc = []
	nyc.append(["arn","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	nyc.append(["got","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDR09UcAGCAQsI____________AUABSAGYAQI"])
	nyc.append(["osl","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDT1NMcAGCAQsI____________AUABSAGYAQI"])
	nyc.append(["cph","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	nyc.append(["ber","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	nyc.append(["fra","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	nyc.append(["par","https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	nyc.append(["lon","https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	for a,val in enumerate(nyc):
		nyc[a].insert(0,"nyc")
	
	bos = []
	bos.append(["arn","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	bos.append(["got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	bos.append(["osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	bos.append(["cph","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	bos.append(["ber","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	bos.append(["fra","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	bos.append(["par","https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	bos.append(["lon","https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	for a,val in enumerate(bos):
		bos[a].insert(0,"bos")

	#mas = [was+nyc+bos]
	mas = []
	app = [was,nyc,bos]
	for a,val in enumerate(app):
		for b,val2 in enumerate(val):
			tem = []
			tem.append([val2[0],val2[1]])
			tem.append([val2[2]])
			mas.append(tem)


	mas.append([["arn", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMDZteHMSCjIwMjEtMDctMjhyDAgDEggvbS8wcmg2a3ABggELCP___________wFAAUgBmAEC"])
	mas.append([["arn", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokagcIARIDQVJOEgoyMDIxLTA3LTI4cg0IAxIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQI"])
	mas.append([["arn", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQVJOEgoyMDIxLTA3LTI4cgcIARIDQk9TcAGCAQsI____________AUABSAGYAQI"])
	mas.append([["got", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDR09UEgoyMDIxLTA3LTI4cgwIAxIIL20vMHJoNmtwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["got", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokagcIARIDR09UEgoyMDIxLTA3LTI4cg0IAxIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQI"])
	mas.append([["got", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDR09UEgoyMDIxLTA3LTI4cgcIARIDQk9TcAGCAQsI____________AUABSAGYAQI"])
	mas.append([["osl", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDT1NMEgoyMDIxLTA3LTI4cgwIAxIIL20vMHJoNmtwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["osl", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokagcIARIDT1NMEgoyMDIxLTA3LTI4cg0IAxIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQI"])
	mas.append([["osl", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDT1NMEgoyMDIxLTA3LTI4cgcIARIDQk9TcAGCAQsI____________AUABSAGYAQI"])
	mas.append([["cph", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQ1BIEgoyMDIxLTA3LTI4cgwIAxIIL20vMHJoNmtwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["cph", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokagcIARIDQ1BIEgoyMDIxLTA3LTI4cg0IAxIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQI"])
	mas.append([["cph", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQ1BIEgoyMDIxLTA3LTI4cgcIARIDQk9TcAGCAQsI____________AUABSAGYAQI"])
	mas.append([["ber", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQkVSEgoyMDIxLTA3LTI4cgwIAxIIL20vMHJoNmtwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["ber", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokagcIARIDQkVSEgoyMDIxLTA3LTI4cg0IAxIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQI"])
	mas.append([["ber", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQkVSEgoyMDIxLTA3LTI4cgcIARIDQk9TcAGCAQsI____________AUABSAGYAQI"])
	mas.append([["fra", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDRlJBEgoyMDIxLTA3LTI4cgwIAxIIL20vMHJoNmtwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["fra", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokagcIARIDRlJBEgoyMDIxLTA3LTI4cg0IAxIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQI"])
	mas.append([["fra", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDRlJBEgoyMDIxLTA3LTI4cgwIAxIIL20vMDFjeF9wAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["par", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMDVxdGoSCjIwMjEtMDctMjhyDAgDEggvbS8wcmg2a3ABggELCP___________wFAAUgBmAEC"])
	mas.append([["par", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhopagwIAxIIL20vMDVxdGoSCjIwMjEtMDctMjhyDQgDEgkvbS8wMl8yODZwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["par", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjEtMDctMjhyBwgBEgNCT1NwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["lon", "was"],"https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMDRqcGwSCjIwMjEtMDctMjhyDAgDEggvbS8wcmg2a3ABggELCP___________wFAAUgBmAEC"])
	mas.append([["lon", "nyc"],"https://www.google.com/travel/flights/search?tfs=CBwQAhopagwIAxIIL20vMDRqcGwSCjIwMjEtMDctMjhyDQgDEgkvbS8wMl8yODZwAYIBCwj___________8BQAFIAZgBAg"])
	mas.append([["lon", "bos"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDRqcGwSCjIwMjEtMDctMjhyBwgBEgNCT1NwAYIBCwj___________8BQAFIAZgBAg"])


	for a,val in enumerate(mas):
		if type(val[1])==str:
			mas[a][1] = [mas[a][1]]


	for a,val in enumerate(mas):
		print ("val",val)
	

	dep = whi("depart,1 for only usa, 2 for only europe")
	arr = whi("arrive,blank for other")

	usa = ["was","nyc","bos"]
	eur = []
	eur.append("arn")
	eur.append("got")
	eur.append("osl")
	eur.append("cph")
	eur.append("ber")
	eur.append("fra")
	eur.append("par")
	eur.append("lon")
	
	rig = []
	rig.append(["1",usa,eur])
	rig.append(["2",eur,usa])

	for a,val in enumerate(rig):
		if dep[0]==val[0]:
			dep = val[1]
			if len(arr)==0:
				arr = val[2]



	print (dep,arr)
	
	che = []
	che.append(["thr",["arn","got","ber"]])
	che.append(["fiv",["arn","got","cph","osl","ber"]])
	whe = []
	whe.append(dep)
	whe.append(arr)
	for a, val in enumerate(whe):
		new=[]
		for b,val2 in enumerate(val):
			print ("val2",val2)
			new.append(matn([val2,che,0,1]))
		whe[a]=new
		rid =[]
		for b,val2 in enumerate(whe[a]):
			if type(val2)==list:
				for c,val3 in enumerate(val2):
					whe[a].append(val3)
				rid.append(b)
				whe[a].pop(b)
	dep = whe[0]
	arr = whe[1]
	print (dep,arr)
	
	

	"""
	if "thr" in dep:
		dep = ["arn","got","ber"]
	if "thr" in arr:
		arr = ["arn","got","ber"]		
	if "fiv" in dep:
		dep = ["arn","got","cph","osl","ber"]
	if "fiv" in arr:
		arr = ["arn","got","cph","osl","ber"]		
	"""
	
	print (dep)
	print (arr)
	com = []
	for a,val in enumerate(dep):
		for b,val2 in enumerate(arr):
			new = [val,val2]
			com.append(new)
	#print (com)
	#print (mas)
	url = []
	for a,val in enumerate(com):
		for b,val2 in enumerate(mas):
			if val==val2[0]:
				url.append(val2[1][0])
				print (val2)
				break
	print (url)
	num4([url,1])
	for a,val in enumerate(url):
		if a==0:
			for b,val2 in enumerate(url):
				hod3(["ctrl","f",1,1])
				"""
				wri("stop",1)
				but(["esc"],0,0)
				hod3(["shift","tab",2,1])
				but(["enter"],0,0)
				"""
				wri("economy",1)
				but(["esc"],0,0)
				but(["tab"],0,0)
				but(["tab"],0,0)
				but(["tab"],0,0)
				but(["tab"],0,0)
								

				#cf_este("stop")
				if b<len(url)-1:
					hod3(["ctrl","pagedown",1,1])
				if b==len(url)-1:
					pgu(len(url),1)
		#cf_ee("price graph")
		"""
		if a<len(url)-1:	
			hod3(["ctrl","pagedown",1,1])
			"""

inp = []
fln2(inp)