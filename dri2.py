exec(open('util.py').read())
def dri2(inp):
	
	import psutil

	#print("All disk partitions: ")
	lis = psutil.disk_partitions()
	for a,val in enumerate(lis):
		print (type(val))
	pri(lis)

inp = []
dri2(inp)