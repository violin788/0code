exec(open('util.py').read())
def reddit(inp):
	#shutil.rmtree()
	#directory = "C:\\Users\\-\\AppData"
	directory = "C:\\Users\\--\\AppData"
	folders = os.listdir(directory)
	for a,val in enumerate(folders):
		specific = directory+"\\"+val
		specific2 = specific+"\\"+"Mozilla"
		files = os.listdir(specific2)
		for b,valb in enumerate(files):
			correct = specific2+"\\"+valb
			os.remove(correct)
		print(specific)
		shutil.rmtree(specific2)
		#os.rmdir(specific2)
	#print(folders)

inp = []
reddit(inp)