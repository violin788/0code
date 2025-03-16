exec(open('util.py').read())
def dri(inp):

	import win32file
	res = win32file.GetDriveType("C:/")
	print(res)
	exec(open('util.py').read())
	fil = "C:\\Users\\-\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\ssd_checker.py"
	exec(open(fil).read())

	from ssd_checker import is_nt_ssd
	res2 = is_nt_ssd("C:/")
	#from ssd_checker import is_ssd

	#is_ssd('/path/to/file-or-dir-or-dev')
	#val = is_ssd('/C:\\')

inp = []
dri(inp)