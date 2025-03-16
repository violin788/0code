exec(open('util.py').read())
def rename(inp):

	folder = os.getcwd()
	earn_folder = folder+"\\earn"
	earn_list = os.listdir(earn_folder)
	for a,val in enumerate(earn_list):
		if ".." in val:
			print(val)
			new_name = val.replace("..","--")
			print(new_name)
			old_file = earn_folder+"\\"+val
			new_file = earn_folder+"\\"+new_name
			os.rename(old_file,new_file)
	#pri(earn_list)


	
inp = []
rename(inp)