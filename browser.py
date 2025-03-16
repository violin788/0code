exec(open('util.py').read())
def bro(con,cor):
	con = rea4([con,'txt'])
	ray = []
	for a,val in enumerate(cor):
		ray.append([val[0],val[0]])

	#ray.append(["fir","fir"])
	#ray .append(["chr","chr"])
	bro = ""
	for a,val in enumerate(ray):
		if val[0] in con:
			bro = val[1]

	for a,val in enumerate(cor):
		if bro==val[0]:
			val[1](val[2])
			break
inp = []
bro(inp)