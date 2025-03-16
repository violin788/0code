exec(open('util.py').read())
def ne7(ray):

	pos = pyautogui.position()
	print (pos)
	#sys.exit()

	
	def mat(inp):
		ray = inp[0]
		loo = inp[1]
		ide = inp[2]
		bac = inp[3]
		for a,val in enumerate(ray):
			if val[ide]==loo:
				return val[bac]
				break

	inp = []
	inp.append("location of new window")
	inp = fol2(inp)
	inp=inp[0][1]
	"""
	sid = []
	sid.append(["ru","l"])
	sid.append(["ll""l"])
	sid.append(["rd","r"])
	sid.append(["ld""r"])
	"""

	#sid = mat([sid,inp,0,0])
	
	new = ""
	if "r" in inp:
		new = "right"
	if "l" in inp:
		new = "left"

	print (new)
	#sys.exit()

	#alt(1,1)
	sw("chrome.exe",1)

	htb("ctrl","shift","n",1,1)
	alt(1,1)
	af4(1,1)
	"""
	hod3(["alt","space",1,0])
	dow = 5
	for a in range(0,dow):
		but3([["down"],0,0])
	but3([["enter"],0,2])
	"""
	"""
	pyautogui.keyDown("win")
	for a,val in enumerate(1):
	#for a in range(0,len(loc)):
		#but(val,0,0)
		but3([[new],0,0])
	pyautogui.keyUp("win")
	"""

	hod3(["win",new,1,1])

	vax = []
	vax.append(["right",1000])
	vax.append(["left",350])
	pox = mat([vax,new,0,1])
	

	pyautogui.moveTo(pox, 725)	
	pyautogui.mouseDown()
	pyautogui.moveTo(pox, 360)
	pyautogui.mouseUp()
	time.sleep(1)
	
	if "d" in inp:
		pyautogui.moveTo(pox, 31)	
		pyautogui.mouseDown()
		time.sleep(1)
		pyautogui.moveTo(pox, 380)
		pyautogui.mouseUp()

	sys.exit()
	


	ray = "ray"	
	new([1,ray])

	new([0,["chr","r"]])
	sys.exit()

	

	inp = []
	inp.append("location of new window")
	inp = fol2(inp)
	inp=inp[0][1]
	"""
	sid = []
	sid.append(["ru","l"])
	sid.append(["ll""l"])
	sid.append(["rd","r"])
	sid.append(["ld""r"])
	"""

	#sid = mat([sid,inp,0,0])
	
	new = ""
	if "r" in inp:
		new = "r"
	if "l" in inp:
		new = "l"

	print(inp)

	#ray = 
	#new([["chr",new],ray])

	new([0,["chr",new]])
	
	
	sys.exit()
	pos = pyautogui.position()
	print (pos)


	#sys.exit()

	ray = "ray"	
	
	#new([1,ray])
	

	pos = pyautogui.position()
	print (pos)

	loc = []
	loc.append(["ru"])
	loc.append(["rd"])
	loc.append(["lu"])
	loc.append(["ld"])

	
	vax = []
	vax.append(["r",1000])
	vax.append(["l",350])

	
	pox = mat([vax,"l",0,1])
	print (pox)
	alt(1,1)
	pyautogui.moveTo(pox, 725)	
	pyautogui.mouseDown()
	pyautogui.moveTo(pox, 360)
	pyautogui.mouseUp()
	


	vax = []
	vax.append(["d",15])
	vax.append(["l",350])


	sys.exit()
	
	#
	"r"
	"l"
	"u"
	"d"

	#pyautogui.moveTo(100, 200)

	pyautogui.moveTo(1000, 725)

	sys.exit()

	
	for a in range(1,10):
		os.mkdir(str(a))
		
	sys.exit()
		

	dri = os.getcwd()
	dri = dri[0:dri.find("\\")]

	print (dri)
	sys.exit()

	fol = "Computer\\LG L355DL\\Internal shared storage\\Download"
	lis = os.listdir(fol)

	print (lis)

	sys.exit()


	#"Computer\LG L355DL\Internal shared storage\Download"


	#new.append([cf_etste3,["log in"]])
	alt(1,1)
	cf_etste3(["log in"])
	sys.exit()
	ray = ["aaa","bbb","ccc"]
	bac = []
	for a,val in enumerate(ray):
		if len(val)>2 and a>0 and a<len(ray)-1:
			#if a>0:
			bac.append("page")
	print (bac)


						


	ray = [1,2]

	for a,val in enumerate(ray):
		if val==1:
			ray.append(3)
		print (val)
	sys.exit()


	ray = ["a","b"]
	opu2([ray,1])
	sys.exit()
	new([0,["chr","r"]])
	sys.exit()		


	sw("cop.txt",1)
	af4(1,1)
	"""
	def ini(inp):
		#l = inp[1]
		#w = inp[0]
		loc = inp[0]
		os.startfile(loc)
		#time.sleep(w)	

	ray = []
	ray.append([ini,["skype.lnk"]])
	for a,val in enumerate(ray):
		print (val)
		print (val[1][0])
		val[0](val[1])
		"""

inp = []
ne7(inp)