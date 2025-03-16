exec(open('util.py').read())
def vio(inp):
	inp = inp
	hod3(["alt","tab",1,1])
	pyautogui.click()
	
	url= []
	url.append("https://www.freeecardgreeting.net/home/violin_html5.php?NSvalue=twinkle+twinkle")
	sou = []
	sou.append(["A","h"])
	sou.append(["B","j"])
	sou.append(["C","a"])
	sou.append(["D","s"])
	sou.append(["E","d"])
	sou.append(["F","f"])
	sou.append(["G","g"])

	son = ""
	son = son + "CCCGEEEC"
	son = son + "CEGGFED"
	son = son + "DEFFEDEC"
	son = son + "CEDGBDC"


	bac = ""
	for a,val in enumerate(son):
		for b,val2 in enumerate(sou):
			if val==val2[0]:
				dow = val2[1]
				bac = bac+dow
				#pyautogui.press(dow)
				print(dow)
				#time.sleep(1)
				break
		#sen = 
	print (bac)

inp = []
vio(inp)