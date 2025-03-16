exec(open('util.py').read())
def ram(inp):

	import psutil
	# gives a single float value
	print(psutil.cpu_percent())
	# gives an object with many fields
	print(psutil.virtual_memory())

	
inp = []
ram(inp)