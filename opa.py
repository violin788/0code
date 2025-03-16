exec(open('util.py').read())
def opa(inp):
	sof = rea4(["bro",'txt'])[0:3]
	ope = []
	ope.append(["fir",cf_ete,"open"])
	ope.append(["chr",cf_ee,"open"])
	cor = matn([sof,ope,0,1])
	var = matn([sof,ope,0,2])
	ray = inp[0]
	tab = inp[1]
	tac = inp[2]
	tex = ""
	print (ray)
	for a,val in enumerate(ray):
		if "http" not in val:
			if "www." not in val:
				val = "www."+val
			ray[a] = "https://"+val
	ray = ray[::-1]
	for a,val in enumerate(ray):
		tex = tex+"x.push(\""+val+"\");\n\t\t"
	print (tex)
	rep = "___rep___"
	con = rea4(["opb",'txt'])
	con = con.replace(rep,tex)
	fil = "opa.html"
	print (fil)
	new = open(fil,"w")
	new.write(con)
	new.close()
	print (con)
	loc = upd([0])
	loc = loc+"\\"+fil
	ope = [loc]
	cot([ope,tac,1])
	cf_ete("open")
	time.sleep(1)
	pgu(2,1)		
	hod3(["ctrl","f4",1,0])
inp = []
opa(inp)