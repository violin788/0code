exec(open('util.py').read())
def memory(inp):


	import psutil
	processes = psutil.process_iter()
	for process in processes:
	    print(f"Process ID: {process.pid}, Name: {process.name()}")	 	
	


	# Importing the library
	import psutil
	 
	# Getting % usage of virtual_memory ( 3rd field)
	print('RAM memory % used:', psutil.virtual_memory()[2])
	# Getting usage of virtual_memory in GB ( 4th field)
	print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)

	
inp = []
memory(inp)