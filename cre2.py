exec(open('bas.py').read())
def cre():
	"""
	con = rt("cre")
	print (con)
	ray = []
	ray.append(["file name"])
	for a in range(0,len(ray)):
		pro = ray[a][0]
		pro = pro+" = "
		ray[a].append(input(pro))
	fil = ray[0][1]
	print (fil)
	"""

	con = rt("cre")
	#print (con)
	fil = input("new file name = ")
	if fil=="cre":
		print ("can't replace")
		sys.exit()
	con = con.replace("cre",fil)
	fil2 = fil+".py"
	fi = open(fil2, "w")
	fi.write(con)
	fi.close()
	#fil2 = fil
	sw(fil2,1)
	but(["down","down","right"],0,0)



cre()