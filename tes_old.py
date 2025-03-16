exec(open('util.py').read())
def tes(inp):


	#fol = "B:\\Users\\-\\Downloads"
	fol = upd([1])+"Downloads"

	lis = os.listdir(fol)

	rep = "yt5s.com - "
	for a, val in enumerate(lis):
		if rep in val:
			old = fol+"\\"+val
			nam = val.replace(rep,"")
			new = fol+"\\"+nam
			os.rename(old, new)
	#sye()

	ray = []
	ray.append(["fir",7,"firefox.lnk"])
	ray.append(["chr",15,"chrome.lnk"])
	fol = os.getcwd()
	#fol = fol.replace("0c","Downloads")
	lis = os.listdir(fol)
	app = ".txt"
	for a,val in enumerate(ray):
		val2 = val[0]
		fin = val2+app
		if fin not in lis:
			new = open(fin,"w")
			new.write("")
			new.close() 
	che = inp[0]
	tex = rea4([che,'txt'])
	man = len(tex)
	if man==0:
		lau = mat2([ray,che,0,2])
		wai = mat2([ray,che,0,1])
		sw(lau,wai)
		hod3(["alt","f4",1,0])
		
		from datetime import datetime
		tim = datetime.now()
		cur = tim.strftime("%H:%M:%S")


		fin = che+".txt"
		new = open(fin,"w")
		new.write(cur)
		new.close()

inp = []
tes(inp)