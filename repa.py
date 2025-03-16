mexec(open('util.py').read())
def repa(inp):
	
	try:
		os.mkdir("code") 
	except:
		print("code dir already exists")
	current_folder = os.getcwd()
	download_folder = current_folder.replace("code","Downloads")
	file_to_copy = download_folder+"\\code.7z"
	print(file_to_copy)
	new_location = file_to_copy.replace("Downloads","code")
	shutil.copy(file_to_copy,new_location)

	import py7zr

	archive = py7zr.SevenZipFile('code.7z', mode='r')
	archive.extractall(path="code")
	archive.close()

	temp_folder = current_folder+"\\code"
	#lis_folder = current_folder+"\\code"
	files_from_7z = os.listdir(temp_folder)

	didnt_work = []
	for a,val in enumerate(files_from_7z):
		old_file = temp_folder+"\\"+val
		new_file = current_folder+"\\"+val
		try: 
			shutil.copy(old_file,new_file)
		except:
			didnt_work.append(old_file)
	pri(didnt_work)

	os.remove("code.7z")
	os.remove("code")

	sye()


inp = []
repa(inp)