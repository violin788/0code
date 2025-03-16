exec(open('util.py').read())
def amt(ray):
	def cop(inp):
		ray = inp[0]
		num = inp[1]
		fil = "cop.txt"
		if num==0:
			tex = ""
			for a,val in enumerate(ray):
				tex = tex+val+"\n"
			f= open(fil,"w")
			f.write(tex)
			f.close() 
			sw("cop.txt",1)
		if num>0:
			alt(1,1)
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		but(["down","up"],0,0)
		if num<len(ray)-1: 
			hod3(["alt","tab",1,0])
		if num==len(ray)-1: 
			af4(1,1)
		hod3(["ctrl","v",1,0])
		num = num+1
		return num
	
	inp = []
	inp.append("from")
	inp.append("to")
	inp.append("month")
	inp.append("day")
	
	inp = fol(inp)
	print (inp)
	
	dep = inp[0]
	arr = inp[1]	
	mon = inp[2]	
	day = inp[3]
	dat = mon+"/"+day+"/2021"
	

	url = "https://www.amtrak.com/home.html"
	urr = []
	urr.append(url)

	def num4([ray,wai]):
		if len(ray)>0:
			nu(ray,1)
			pgu(len(ray),1)
			time.sleep(wai)

	
	way = 0

	if way==0:
		num4([urr,1])
		time.sleep(3)
	if way==1:
		alt(1,1)

	tex = []
	tex.append(dep)
	tex.append(arr)
	tex.append(dat)


	cf_e3(["use p"])
	but3([["tab","tab"],0,0])
	time.sleep(1)
	num = cop([tex,0])
	but3([["tab","tab"],0,0])
	num = cop([tex,num])
	but3([["tab"],0,0])
	num = cop([tex,num])
	but3([["tab","tab","tab","tab","enter"],0,0])
	

	
inp = []
amt(inp)