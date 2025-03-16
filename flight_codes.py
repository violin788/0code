exec(open('util.py').read())
def nel(ray):
	eur = []
	eur.append(["arn","/m/06mxs"])
	eur.append(["got","GOT"])
	eur.append(["osl","/m/05l64"])
	eur.append(["cph","CPH"])
	eur.append(["ber","BER"])
	eur.append(["fra","/m/02z0j"])
	eur.append(["par","/m/05qtj"])
	eur.append(["lon","/m/04jpl"])

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
	


	bac = []
	for a,val in enumerate(eur):
		if a==0:
			alt(1,1)
			sw("nel.txt",1)
			alt(1,1)
		for b,val2 in enumerate(usa):
			
			hod3(["alt","d",1,0])
			hod3(["ctrl","c",1,0])
			alt(1,1)
			dep = val
	
			tem = []
			tem.append(dep)
			tem.append(val2)
			tem = str(tem)
			tem = "mat.append(["+tem+",\""
			tem = tem.replace("'","\"")
			wri(tem,1)
			hod3(["ctrl","v",1,1])
			wri("\"])",1)
			key([["enter",1,0,0]])
			alt(1,1)
			hod3(["ctrl","pagedown",1,1])

			"""
			mat.append()


		wri("bos.append([\""+des+"\",\"",1)
		#key([["enter",1,0,0]])
		hod3(["ctrl","v",1,1])
		wri("\"])",1)
		key([["enter",1,0,0]])
		alt(1,1)
		hod3(["ctrl","pagedown",1,1])
		"""






		

inp = []
nel(inp)