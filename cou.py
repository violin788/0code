exec(open('util.py').read())
def cou(ray):
	
	#inp =int(input("num = "))
	inp = 6
	nam = "cou"
	for a in range(0,inp):
		if a==0:
			at(1,1)
			fil = nam+'.txt'
			f= open(nam,"w")
			f.write("")
			f.close() 

			#subprocess.Popen(['wordpad.exe', fil])
	

			os.startfile(fil)
			time.sleep(2)
		

			#xsw(fil,1)
			at(1,1)	
			#sys.exit()
		hod3(["alt","d",1,0])
		hod3(["ctrl","c",1,0])
		at(1,1)	
		hod3(["ctrl","v",1,0])
		#but3(["enter",0,0])		
		pyautogui.press("enter")
	
		at(1,1)	
		hod3(["ctrl","pageup",1,0])
		#if a==1:
		#	sys.exit()
	

	at(1,1)


	ray = ray

inp = []
cou(inp)