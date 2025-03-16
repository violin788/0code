exec(open('util.py').read())
def map3(inp):
	#pla = str(input("place = "))
	pla = inp[0]
	mat = []
	mat.append(["vir","virginia"])
	mat.append(["hay","haynesville, va"])
	mat.append(["fre","fredericksburg, va"])

	mat.append(["fbg","fredericksburg, va"])

	mat.append(["arl","arlington, va"])
	mat.append(["was","washington dc"])
	mat.append(["sil","silicon valley"])
	mat.append(["nov","northern+virginia/@38.835214,-77.3281126,85722m/data=!3m1!1e3"])
	mat.append(["sto","stockholm"])

	ski = []
	ski.append("nov")

	res = che(ski,pla)
	print (res)
	
	
	
	def cf_ee(text):
		hod3(["ctrl","f",1,1])
		wri(text,1)
		but(["esc","enter"],0,0)	




	for a in range(0,len(mat)):
		if pla==mat[a][0]:
			pla = mat[a][1]
			break
	url = "https://www.google.com/maps/place/"+pla
	neu6(url,1,5)
	
	if res==0:
		cf_ee(pla)
		time.sleep(2)
		cf_ete2("satell")

inp = []
map3(inp)