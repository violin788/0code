exec(open('util.py').read())
def ebal(inp):
	url = "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru="
	usn = "violin78@protonmail.com"
	pas = "Viovio1!"
	ray = []
	eba = []
	"""
	eba.append([hod3,["alt","tab",1,1]])	
	eba.append([hod3,["alt","tab",2,1]])	
	"""
	eba.append([hod3,["ctrl","t",1,1]])	
	eba.append([url])
	eba.append([but3,[["enter"],0,3]])
	eba.append([cf_et3,["account",1,0]])
	eba.append([usn])
	#eba.append([neu3,[url,3,5]])
	#eba.append([cf_et5,["account",1,1]])	
	#eba.append([usn])
	eba.append([but3,[["enter"],0,2]])
	"""
	eba.append([usn])
	eba.append([but3,[["enter"],0,3]])
	"""
	eba.append([pas])
	eba.append([but3,[["enter"],0,0]])
	#return ray
	ray.append(eba)
	nav(ray)


inp = []
ebal(inp)