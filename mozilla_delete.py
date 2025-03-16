exec(open('util.py').read())
def mozilla_delete(inp):
	
	base_directory = "C:\\Users\\--\\AppData"
	folders = ["Local","LocalLow","Roaming"]
	for a,val in enumerate(folders):
		new_directory = base_directory+"\\"+val
		directory_to_delete = new_directory+"\\"+"Mozilla"
		print (directory_to_delete)
		shutil.rmtree(directory_to_delete)

	
inp = []
mozilla_delete(inp)