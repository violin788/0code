exec(open('util.py').read())
def flin(ray):
	usa = []
	usa.append(["was","/m/0rh6k"])
	usa.append(["nyc","/m/02_286"])
	usa.append(["bos","BOS"])
	#usc.append(["sfo","SFO"])
	eur = []
	
	eur.append(["arn","/m/06mxs"])
	eur.append(["got","GOT"])
	eur.append(["osl","/m/05l64"])
	eur.append(["cph","CPH"])
	eur.append(["ber","BER"])
	eur.append(["fra","/m/02z0j"])
	eur.append(["par","/m/05qtj"])
	eur.append(["lon","/m/04jpl"])
	
	"""
	eur.append(["fra","/m/02z0j"])
	eur.append(["par","/m/05qtj"])
	#eur.append(["fra","TXL"])
	eur.append(["ams","/m/0k3p"])
	eur.append(["lon","/m/04jpl"])
	eur.append(["vie","/m/0fhp9"])
	"""

	way = int((input("1 for US to Europe, 2 for Europe to US = ")))
	new = []
	new.append([1,[usa,eur]])
	new.append([2,[eur,usa]])


	ray = []
	for a,val in enumerate(new):
		if way==val[0]:
			ray = val[1]
			for b,val2 in enumerate(ray):
				ray[b]=[ray[b]]
			break
	ray[0].insert(0,"dep")
	ray[0].insert(1,"from")
	ray[1].insert(0,"arr")
	ray[1].insert(1,"to")
	print ("ray",ray)
	#sys.exit()

	"""
	ray = []
	new = []
	new.append("dep")
	new.append("from")
	new.append(flo[0])
	ray.append(new)
	new = []
	new.append("arr")
	new.append("to")
	new.append(flo[1])
	ray.append(new)
	"""
	for a, val in enumerate(ray):
		inq = val[1]
		spe = whi(inq+" specific airports? = ")
		air = []
		if len(spe)>0:
			air = mat2(spe,val[2],0,1)
		else:
			for b,cor in enumerate(val[2]):
				air.append(cor[1])
		val.append(spe)
		val.append(air)
		print ("val",val)
	print ("ray",ray)
	print ("ray[00][4]",ray[0][4])
	from datetime import date
	today = date.today()
	d1 = today.strftime("%Y-%m-%d")
	urr = []
	loc = 4
	for a,val1 in enumerate(ray[0][loc]):
		for b,val2 in enumerate(ray[1][loc]):
			new = "https://www.google.com/flights#flt="+val1+"."+val2+"."+d1+";c:USD;e:1;m:pf;sd:1;t:f;tt:o"			
			urr.append(new)
	dr(urr)
	nu(urr,1)
	pg2(urr,"price gra")
	pgup(len(urr)-1,0)
inp = []
flin(inp)