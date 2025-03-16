exec(open('util.py').read())
def pow(inp):
	import os
	bac = input("Do you wish to shutdown your computer ? (1 for yes / blank for no): ")  
	if bac=="1":
		ray = []
		ray.append("fir")
		ray.append("chr")
		fol = os.getcwd()
		#fol = fol.replace("0c","Downloads")
		lis = os.listdir(fol)
		app = ".txt"
		for a,val in enumerate(ray):
			fin = val+app
			#if fin not in lis:
			new = open(fin,"w")
			new.write("")
			new.close() 
		os.system("shutdown /s /t 1")
	"""
	bac = input("Do you wish to shutdown your computer ? (yes / no): ")
	  
	if shutdown == 'no':
	    exit()
	else:
		"""
inp = []
pow(inp)