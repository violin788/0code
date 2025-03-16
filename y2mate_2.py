exec(open('util.py').read())
def y2m2(ray):

	inp = []
	inp.append("where to start, 1 to get, 2 to move, 3 to delete")
	inp = fol2(inp)
	print (inp)
	beg = int(inp[0][1])-1
	dri = os.getcwd()
	dri = dri[0:dri.find("\\")]
	mov =dri+"\\Users\\-\\Downloads\\mov"
	dow = dri+"\\Users\\-\\Downloads"

	def y2m1(inp):


		#not mp3
		url = ges(rt("y2m"),"\n")
		tex = []
		bas = []
		bas.append("https://www.go-mp3.com/en20")
		for a,val in enumerate(url):
			if a==0:
				ope = []
				for b,val2 in enumerate(url):
					ope.append("https://www.go-mp3.com/en20")
					tex.append(val2)
				#cot([ope,1,1])
			


			cot([bas,1,1])
			time.sleep(3)
			cf_et3(["paste",1,0])
			cop([tex,a])
			key([["enter",1,0,2]])
			cf_ee("download the")
			time.sleep(1)
			#key([["enter",1,0,1]])
			hod3(["ctrl","f4",1,1])
			#key([["enter",1,0,1]])
			cf_ee("download the")
			if a<len(url)-1:
				hod3(["ctrl","pagedown",1,1])
		


				"""
			
		#second one
		#fol = inp[0]
		#ray = ray
		bas = "https://www.y2mate.com/youtube/"
		url = ges(rt("y2m"),"\n")
		print (url)
		for a,val in enumerate(url):
			print (val)
			val = val.replace("https://www.youtube.com/watch?v=","https://youtubetomp3music.com/en26/download?url=")
			url[a] = val
		cot([url,1,1])
		time.sleep(5)			
		for a,val in enumerate(url):
			cf_eee("convert")
			if a<len(url)-1:
				hod3(["ctrl","pagedown",1,1])
		pgu(len(ray),1)		
		con =str(input("click to continue = "))
		alt(1,1)
		for a,val in enumerate(url):
			hod3(["ctrl","f",1,1])
			key([["esc",1,0,0],["tab",1,0,0],["enter",1,0,1]])
			if a<len(url)-1:
				hod3(["ctrl","pagedown",1,1])
				
		


		


		#old y2m
		cot([url,1,1])
		sye()
		inp = fol2(["type, mp3 or vid"])
		typ = inp[0][1]
		mat = []
		mat.append(["mp3",["mp3",".mp3"]])
		mat.append(["vid",["video",".mp4"]])
		for a, val in enumerate(mat):
			if typ==val[0]:
				cor= val[1]
		fir = cor[0]
		sec = cor[1]
		print (url)
		num4([url,1])
		for a,val in enumerate(url):
			cf(fir,1)
			key([["enter",1,0,0],["esc",1,0,0],["enter",1,0,0]])
			if sec==".mp4":
				#"360p"
				#cf_et3(["360p",1,1])
				cf("360p",1)
			cf("download",1)
			key([["enter",1,0,0],["esc",1,0,0],["enter",1,0,0]])
			cf("download "+sec,1)
			key([["enter",1,0,0],["esc",1,0,0],["enter",1,0,0]])
			if a<len(url)-1:
				hod3(["ctrl","pagedown",1,1])
				"""
	def y2m2(inp):
		fol = inp[0]
		#fol = "A:\\Users\\-\\Downloads"
		lis = os.listdir(fol)
		rep = "y2mate.com - "
		las = []
		for a,val in enumerate(lis):
			if rep in val:
				old = fol+"\\"+val
				new = old.replace(rep,"")
				new = new.replace("\\Downloads","\\Downloads\\mov")
				print (val)
				#os.rename(old, new)
				shutil.copy(old, new)
				os.remove(old)

				las.append(val)
		tex = ""
		for a,val in enumerate(las):
			tex = tex+val+"\n"
		new = open("las.txt","w")
		new.write(tex)
		new.close() 
		mov = ges(rt("las"),"\n")
		lis = os.listdir(fol)
		#fol = "A:\\Users\\-\\Downloads\\mov"
		fol = fol+"\\mov"

		sw(fol,2)
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		hod3(["shift","tab",1,1])
		wri("lg",1)
		#key([["right",3,1,0]])
		key([["right",1,1,0],["down",1,1,0],["right",1,1,0]])
		wri("down",1)
		key([["enter",1,0,3]])
		hod3(["ctrl","v",1,0])

	def y2m3(ray):
		fol = ray[0]
		lis = os.listdir(fol)
		for a,val in enumerate(lis):
			rem = fol+"\\"+val
			os.remove(rem)

	sta = []
	sta.append([y2m1,ray])
	sta.append([y2m2,[dow]])
	sta.append([y2m3,[mov]])

	for a,val in enumerate(sta):
		if a<beg:
			continue
		val[0](val[1])
		if a<len(sta)-1:
			
			nex = fol2(["click to continue to stage "+str(a+2)])

	#"where to start, 1 to get, 2 to move, 3 to delete"
	"""
			"""

	




inp = []
y2m2(inp)