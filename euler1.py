exec(open('util.py').read())
def eul1(inp):
	top = 1000
	val1 = 3
	val2 = 5
	lis = []
	add = 0
	for a in range(0,top):
		tes1 = str(a/val1)
		tes2 = str(a/val2)
		print(a,tes1,tes2)
		if ".0" in tes1 or ".0" in tes2:
			add = add+a
			"""


		tes3 = int(tes1)
		tes4 = int(tes2)
		tes5 = tes3-tes1
		tes6 = tes4-tes2
		if tes5==0:
			if tes6==0:
				if a not in lis:
					add = add+a
					lis.append(a)
					"""
	print(add)
inp = []
eul1(inp)