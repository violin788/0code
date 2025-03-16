exec(open('util.py').read())
def services(inp):
	
	import psutil

	def get_running_services():
	    running_services = []
	    for proc in psutil.process_iter(attrs=['name']):
	        try:
	            running_services.append(proc.info['name'])
	        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
	            pass
	    running_services.sort()
	    return running_services

	pri(get_running_services())


	
	
inp = []
services(inp)