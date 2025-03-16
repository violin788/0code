exec(open('util.py').read())
def eba(inp):
	
	sea =str(input("search term = "))
	url1 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
	url2 = sea
	url3 = "&_sacat=0&_sop=15&rt=nc&LH_PrefLoc=3"
	url = url1+url2+url3
	#url = [url]
	#url = [url]
	num4([url,1])


	#https://www.ebay.com/sch/i.html?_from=R40&_nkw=
	#my1016
	#&_sacat=0&_sop=15&rt=nc&LH_PrefLoc=3

	"""
	ray = []
	new = []
	new.append("https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=") 
	new.append("")
	new.append([cf_et5,["account",1,1]])
	new.append("violin78@protonmail.com")
	#new.append([cf_et,[["account"]]])

	#new.append([cf_et5,["account",1,1]])
	#new.append("viovio")
	new.append("Viovio1!")
	ray.append(new)
	

	tex2= ""
	for a in range(0,len(ray)):
		tex2 = tex2+ray[a][2]+"\n"+ray[a][4]+"\n"
		#mer.append(ray[a][1])
		#mer.append(ray[a][3])

	fil2 = "owl3.txt"
	fi = open(fil2, "w")
	fi.write(tex2)
	fi.close()
	

	url = []
	for a in range(0,len(ray)):
		url.append(ray[a][0])
	nu(url,1)
	pgu(len(url),0)
	
	fir = 0

	for a in range(0,len(ray)):
		if a==0:
			subprocess.Popen(['notepad.exe', fil2])
			time.sleep(2)
			#r3(["right","down"])
			r3(["left","down"])
			
		if len(ray[a][1])>0:
			at(1,0)
			ray[a][1][0](ray[a][1][1])
			at(1,0)
		#at(1,1)
		#if a<len(ray)-1:
		hod3(["shift","down",1,0])
		#else:
		#	hod3(["shift","end",1,0])
		hod3(["ctrl","c",1,0])
		but(["right"],0,0)
		hod3(["alt","tab",1,0])
		hod3(["ctrl","v",1,0])
		if len(ray[a][3])>0:
			ray[a][3][0](ray[a][3][1])
		at(1,1)
		if a<len(ray)-1:
			hod3(["shift","down",1,0])
		else:
			hod3(["shift","end",1,0])
		hod3(["ctrl","c",1,0])
		but(["right"],0,0)
		if a<len(ray)-1:
			hod3(["alt","tab",1,0])
		if a==len(ray)-1:
			hod3(["alt","f4",1,0])
		hod3(["ctrl","v",1,0])
		but(["enter"],0,0)
		if a<len(ray)-1:
			hod3(["ctrl","pagedown",1,0])
			at(1,1)
			"""


inp = []
eba(inp)