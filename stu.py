exec(open('util.py').read())
def stu(ray):
	rem =int(input("1 for rem, 0 for leave = "))
	if rem==1:
		fol = os.getcwd()
		fol = fol.replace("0c","Downloads")
		lis = os.listdir(fol)
		for a,val in enumerate(lis):
			if "studiemedel" in val:
				fil = fol+"\\"+val
				print (fil)
				
				os.remove(fil)
		print (fol)
	
	#dri = dri[0:dri.find("\\")]
	ray = ray
	ide = "beslut om studiemedel"
	alt(1,1)
	fir = 0
	for a in range(7,23):
		cf(ide,1)
		if a>0:
			for b in range(0,a):
				#key([["enter",1,0,1]])
				key([["enter",1,0,0]])
		key([["esc",1,0,0]])
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		if fir==1:
			alt(1,1)
		if fir==0:
			alt(2,1)
			fir=1	
		hod3(["ctrl","v",1,0])
		key([["down",1,0,0]])
		alt(1,1)
		key([["enter",1,0,4]])
		key([["tab",8,0,1]])
		key([["enter",1,0,2]])
		hod3(["ctrl","v",1,1])
		alt(1,1)
		hod3(["ctrl","c",1,0])
		key([["down",1,0,0]])
		alt(1,1)
		key([["right",1,0,0],["space",1,0,0]])
		hod3(["ctrl","v",1,0])
		chod3(["ctrl","pageup",1,1])
inp = []
stu(inp)