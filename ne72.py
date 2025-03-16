exec(open('util.py').read())
def ne72(inp):
	print (inp,len(inp))
	pos = pyautogui.position()
	print (pos)
	def mat(inp):
		spe = inp[0]
		ray = inp[1]
		ide = inp[2]
		bac = inp[3]
		for a,val in enumerate(ray):
			if val[ide]==spe:
				return val[bac]
				break
	print (inp)
	coo = []
	coo.append(["ru",1000,725,360])
	coo.append(["rd",1000,0,360])
	coo.append(["lu",350,725,360])
	coo.append(["ld",350,0,360])
	
	#ope = "fir"
	#sof = "chr"
	
	#sof = rea4(["bro",'txt'])[0:3]
	cor = []
	cor.append(["fir","p","firefox.exe"])
	cor.append(["chr","n","chrome.exe"])
	
	let = matn([brs,cor,0,1])
	fil = matn([brs,cor,0,2])

	wai = 1

	swi = 1
	if swi==1:
		sel = "fir"
		if "fir" in sel:
			#fil = "B:\\Program Files\\Mozilla Firefox\\firefox.exe"
			#fil = "B:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

			fil = upd(["dri"])+"Program Files (x86)\\Mozilla Firefox\\firefox.exe"

			let = "p"
			wai = 3



	print (let,fil)
	


	for a,val in enumerate(inp):
		spe = val
		#sw("chrome.exe",1)
		#sw("firefox.exe",1)
		sw(fil,wai)

		htb("ctrl","shift",let,1,1)
		alt(1,0)
		af4(1,0)
		


		new = ""
		print ("spe",spe)
		
		if "r" in spe:
			new = "right"
		if "l" in spe:
			new = "left"
		#hod3(["win",new,1,0])
		hod3(["win",new,1,1])
		#htb("ctrl","shift","n",1,1)
		#htb("ctrl","shift",let,1,1)
		"""
		hod3(["alt","space",1,0])
		key([["down",2,0,0],["enter",1,0,0],["left",1,0,0],["up",1,0,0],["enter",1,0,0]])
		pox = mat([val,coo,0,1])
		sta = mat([val,coo,0,2])
		end = mat([val,coo,0,3])
		pyautogui.moveTo(pox, sta)	
		pyautogui.mouseDown()
		pyautogui.moveTo(pox, end)	
		pyautogui.mouseUp()
		"""

inp = []
ne72(inp)