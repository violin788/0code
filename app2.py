exec(open('util.py').read())
def app2(inp):
	tex = rea4(["app",'txt'])
	lis = gel(tex,"\n")
	new = []
	ski = []
	#ski.append("Episode")
	ski.append("MB")
	ski.append(".")
	ski.append("KB")
	#ski.append("")
	#ski.append("MIB")
	#ski.append("DOWNLOADED")
	#ski.append("PM")
	#ski.append(">")
	#ski.append("<")

	for a,val in enumerate(lis):
		con = 0
		for b,val2 in enumerate(ski):
			if val2 in val:
				con = 1
				break
		val= val.replace("Oo","")
		val= val.replace("oO","")
		if con==1 or len(val)<3:
			continue
		if val in new:
			continue	
		new.append(val)
	new.append("Routeshout 2.0")
	new.sort()
	dis(new)
	
	tex = open("app2.txt","w")
	for a,val in enumerate(new):
		tex.write(val+"\n")
	tex.close()



	#new = []
	#print (tex)

inp = []
app2(inp)