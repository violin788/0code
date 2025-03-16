exec(open('util.py').read())
def flis(ray):
	usa = []
	usa.append(["was","/m/0rh6k"])
	usa.append(["nyc","/m/02_286"])
	usa.append(["bos","BOS"])
	usa.append(["sjc","SJC"])
	usa.append(["sfo","SFO"])
		
	eur = []
	eur.append(["got","GOT"])
	eur.append(["cph","CPH"])
	eur.append(["arn","/m/06mxs"])
	eur.append(["osl","/m/05l64"])
	eur.append(["fra","/m/02z0j"])
	eur.append(["ber","BER"])
	eur.append(["par","/m/05qtj"])
	eur.append(["lon","/m/04jpl"])
	

	tot = usa+eur
	way = 1
	new = []
	new.append([1,[tot,tot]])
	new.append([2,[tot,tot]])

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

	def mat(ray,inp,ind):
		for a,val in enumerate(ray):
			if inp==val[ind]:
				return val
				break
	print ("ray",ray)

	def rep(ori,new):
		bac = []
		
		for a,val in enumerate(ori):
			con = 0
			for b,val2 in enumerate(new):
				if val==val2[0]:
					if type(val2[1])==list:
						for c,val3 in enumerate(val2[1]):
							bac.append(val3)
					if type(val2[1])!=list:
						bac.append(val3)
					break
					con = 1
			if con==1:
				continue
			else:
				bac.append(val)

		#if len(bac)>0:	
		return bac
		"""
	def rep2(ori,new):
		bac = []
		
		for a,val in enumerate(ori):
			con = 0
			for b,val2 in enumerate(new):
				if val==val2[0]:
					val.pop(a)
					if type(val2[1])==list:
						for c,val3 in enumerate(val2[1]):
							val.insert(a+c,val3)
					if type(val2[1])!=list:
						val.insert(a+c,val3)
					break
					con = 1
					
			#if con==1:
			#	continue
			#else:
			#	bac.append(val)
				

		#if len(bac)>0:	
		return bac
		"""
	
	
	new = []
	new.append(["bay",["sjc","sfo"]])


	def mat2(mat,ray,ind1,ind2):
		bac = []
		for a,val1 in enumerate(mat):
			for b,val2 in enumerate(ray):
				print ("val2",val2)
				spe = val2[ind1]
				if val1==spe:
					bac.append(val2[ind2])
		return bac
	for a, val in enumerate(ray):
		print ("val",val)
		inq = val[1]
		spe = whi(inq+" specific airports? = ")
		spe = rep(spe,new)
		print ("spe",spe)
		#sys.exit()
		#spe = rep(spe,new)
		print ("spe",spe)
		#sys.exit()
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

	"""	inp = []
flis(inp)