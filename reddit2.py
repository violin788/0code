exec(open('util.py').read())
def reddit2(inp):
	
	firefox_uninstall = "C:\\Program Files (x86)\\Mozilla Firefox\\uninstall\\helper.exe"
	try:
		start_file([firefox_uninstall,0])
	except:
		skip = "skip"
	#delete mozilla directory in C program files

	#delete google chrome by hand?

	google_directory = "C:\\Program Files (x86)\\Google"
	try:
		shutil.rmtree(google_directory)
	except:
		print("already removed")
	print("removed directory = "+google_directory)
	#delete appdata (cookies) for both mozilla and chrome
	browser_cookie_folders = ["Google","Mozilla"]
	directories = ["Local","LocalLow","Roaming"]
	main_cookie_directory = "C:\\Users\\--\\AppData"
	for a,val in enumerate(directories):
		for b,valb in enumerate(browser_cookie_folders):
			directory_to_delete = main_cookie_directory+"\\"+val+"\\"+valb
			try:
				shutil.rmtree(directory_to_delete)
				print("removed directory = "+directory_to_delete)
			except:
				print("directory does not exist = "+directory_to_delete)
	#delete appdata (cookies) for both mozilla and chrome
	#reinstall chrome and firefox
	to_install = []
	to_install.append("Firefox Setup 100.0-32bit.exe")
	to_install.append("Google_Chrome_(32bit)_v100.0.4896.127.exe")
	download_directory = "C:\\Users\\--\\Downloads"
	for a,val in enumerate(to_install):
		file_to_install = download_directory+"\\"+val
		start_file([file_to_install,0])
	#see what cookies are in chrome = chrome://settings/siteData
	#see what cookies are in firefox = about:preferences#privacy  ..then "manage data"
	
inp = []
reddit2(inp)