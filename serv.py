exec(open('util.py').read())
def serv(inp):
	
	import win32serviceutil

	def get_services():
	    services = win32serviceutil.EnumServicesStatus()
	    service_list = [service[0] for service in services]
	    return service_list

	print(get_services())
	
	
inp = []
serv(inp)