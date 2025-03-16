exec(open('util.py').read())
def get(ray):
	ray = ray

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

	bas = ["https://www.google.com/travel/flights?tfs=CBwQARoaagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhwAYIBCwj___________8BQAFIAZgBAg"]

	def wri(to_write,wait):
		pyautogui.write(to_write)
		time.sleep(wait)


	for a,val in enumerate(eur):
		#num4([bas,1])
		for b,val2 in enumerate(usa):
			arr = val2[0]
			dep = val[0]
			#if dep!="bos":
			#	continue
			

			num4([bas,0])
			#dep = "bos"
			tex = []
			tex.append(arr)
			tex.append(dep)
			#tex.append(arr)
			cf_etst(["where"])
			#cf_et3(["eco",1,0])
			#key([["tab",1,0,0]])
			

			cop([tex,0])
			key([["enter",1,0,0]])
			
			cf_et3(["eco",1,0])
			

			cop([tex,"dep"])
			key([["enter",2,0,0]])
			#wri(val[0],1)
			#cf_este3(["where",1,1])	
			#cf_etst(["where"])
			#cop([tex,"arr"])
			#key([["enter",1,0,1],["tab",1,0,0]])
			#key([["enter",1,0,0],["tab",1,0,0]])
			#wri(val2[0],1)
			#key([["enter",2,0,0]])
			alt(1,1)

			#sys.exit()
			"""

			#wri(val2[0],1)
			sys.exit()
			#hod3(["shift","tab",1,0])
			#cf_etst(["wash"])
			arr = val2[0]
			dep = val[0]
			tex = []
			tex.append(dep)
			tex.append(arr)
			cop([tex,0])
			#time.sleep(1)
			hod3(["shift","tab",2,1])
			
			#wri(dep,1)
			#hod3(["shift","tab",2,0])
			#key([["tab",2,0,0]])

			cop([tex,"dep"])
			#wri(arr,1)
			#key([["tab",1,0,0]])
			cop([tex,"arr"])
			key([["enter",2,0,0]])
			"""
			#sys.exit()
			"""

			print (val2[0])
			print (val[0])
			#wri(val2[0],2)
			
			tex.append(val2[0])
			tex.append(val[0])
			#cop([tex,0])
			hod3(["shift","tab",2,1])
			cop([tex,"pas"])
			3key([["enter",2,0,0]])
			"""

inp = []
get(inp)