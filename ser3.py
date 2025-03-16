exec(open('util.py').read())
def ser3(inp):
	
	gui_list = []
	gui_list.append(["button","server2","server2.py"])
	#gui_list.append(["geometry","200x200"])
	#gui_list.append(["entry","python file","start server","shell_entry0"])
	#gui_list.append(["entry","javascript file","start server","shell_entry1"])
	gen_gui3([gui_list])
	
	
inp = []
ser3(inp)