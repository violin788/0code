exec(open('util.py').read())
def rum(ray):
	for a in range(0,len(ray)):
		ray[a][0](ray[a][1])

inp = []
rum(inp)