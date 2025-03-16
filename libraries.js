exec(open('util.py').read())
def libraries(inp):
	
	to_install = []
	to_install.append("xlsx")
	to_install.append("express")
	to_install.append("open")


	for a,val in enumerate(to_install):
		print(a,len(to_install),val)
		shell(["pip install "+val])
	
inp = []
libraries(inp)