exec(open('util.py').read())
def har2(inp):
	tex = rea4(["har2","txt"])
	print(tex)
	print("")
	new = [" "]
	for a,val in enumerate(new):
		tex = tex.replace(val,"")
	print(tex)
	print("")
	new2 = ""
	ski = ["\n","-"]
	for a in range(0,len(tex)):
		#new2 = tex[a]+" "
		print(tex[a])
		new2 = new2+tex[a]
		#if tex[a]=="\n":
		if tex[a] in ski:
			continue
		new2 = new2+" "
	print("")
	print(new2)
	new3 = new2.replace(" ","\t")
	new3 = new3.replace("\n\n","\n")
	
	print(new3)

	#write txt
	new = open("har2.2.txt","w")
	new.write(new3)
	new.close()


inp = []
har2(inp)