exec(open('util.py').read())
def chrome_delete_files(inp):

	to_delete = []
	to_delete.append("C:\\Program Files (x86)\\Google\\Update\\GoogleUpdate.exe")
	to_delete.append("C:\\Program Files (x86)\\Google\\Update\\1.3.36.372\\GoogleUpdate.exe")
	to_delete.append("C:\\Program Files (x86)\\Google\\Update\\1.3.36.372\\GoogleUpdateBroker.exe")
	to_delete.append("C:\\Program Files (x86)\\Google\\Update\\1.3.36.372\\GoogleUpdateComRegisterShell64.exe")
	to_delete.append("C:\\Program Files (x86)\\Google\\Update\\1.3.36.372\\GoogleUpdateCore.exe")
	to_delete.append("C:\\Program Files (x86)\\Google\\Update\\1.3.36.372\\GoogleUpdateOnDemand.exe")
	for a,val in enumerate(to_delete):
		os.remove(val)
		print(val)
		print("removed")
	
inp = []
chrome_delete_files(inp)