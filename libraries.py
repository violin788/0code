exec(open('util.py').read())
def libraries(inp):
	
	to_install = []
	to_install.append("xlrd")
	to_install.append("json")
	to_install.append("urllib3==1.26.6")
	to_install.append("time")
	to_install.append("xlrd")
	to_install.append("os")
	to_install.append("sys")
	to_install.append("csv")
	to_install.append("pyautogui")
	to_install.append("time")
	to_install.append("datetime")
	to_install.append("xlwt")
	to_install.append("psutil")
	to_install.append("xlsxwriter")
	to_install.append("pandas")
	to_install.append("subprocess")
	to_install.append("shutil")
	to_install.append("math")	

	for a,val in enumerate(to_install):
		print(a,len(to_install),val)
		shell(["pip install "+val])
	
inp = []
libraries(inp)