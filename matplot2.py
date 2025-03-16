exec(open('util.py').read())
def mat2(inp):
	import matplotlib.pyplot as mpl
	ray = []
	ray.append([1,10])
	ray.append([2,20])
	ray.append([3,30])

	def gra(inp):
	#gra([ray])
		ray = inp[0]
		xva = []
		yva = []
		for a,val in enumerate(ray):
			print(val)
			xva.append(val[0])
			yva.append(val[1])
		print("xva",xva)
		print("yva",yva)
		mpl.plot(xva,yva)
		mpl.show()

	gra([ray])

	#mpl.plot([1, 2, 3, 4], [1, 4, 9, 16])
	#mpl.plot(, [1, 4, 9, 16])
	#mpl.show()

	"""

	import matplotlib.pyplot as plt
	plt.plot([1, 2, 3, 4])
	plt.ylabel('y label')
	plt.xlabel('x label')
	plt.show()
	"""	

inp = []
mat2(inp)