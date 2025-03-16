exec(open('util.py').read())
def eul2(inp):
	ray = [1, 2]
	end = 0
	add = 0
	while(end<1):
		le2 = len(ray)
		new = ray[le2-1]+ray[le2-2]
		if new<4000000:
			ray.append(ray[le2-1]+ray[le2-2])
		if new>=4000000:
			break
		tes = rev([str(new)])
		tes2 = tes[0]
		yes = ["0","2","4","6","8"]
		#print(new,tes)
		if tes2 in yes:
			print(new,tes,tes2)
		
			add = add+int(new)
	#pri(ray)
	print(add)
		#ray[le2-1]+ray[le2-2]
	#print(ray)
inp = []
eul2(inp)