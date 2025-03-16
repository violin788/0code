exec(open('util.py').read())
"""
email
media788788@gmail.com,violin78@protonmail.com,cello34@protonmail.com,violin78@mail.com,usa2@email.com
code.7z
C:\\Users\\-\\Downloads\\code.7z

"""
def save(inp):
	naw = []
	def generate_save_file(inp):
		import py7zr
		cwd = os.getcwd()
		lis = os.listdir(cwd)
		#ski = if this in value in lis
		ski = [".exe"]
		#also get rid of, if does not contain.."."
		lis2 = []
		for a,val in enumerate(lis):
			no = 0
			for b,valb in enumerate(ski):
				if valb in val:
					no = 1
					break
			if no==1:
				continue
			if "." not in val:
				no=1
			if no==0:
				lis2.append(val)
		dri = dri_([])
		print(dri)
		acc = acc_([])
		dow = dri+"\\Users\\"+acc+"\\Downloads"
		nam = cuf([])+".7z"
		out = dow+"\\"+nam
		with py7zr.SevenZipFile(out,'w') as archive:
		    for a,val in enumerate(lis2):
		    	archive.write(val)
		    	cen = pro2([a,len(lis2),2])
		    	print(cen,end='\r')
		siz([out])
		time.sleep(1)
	def email(inp):
		emails = gen_emails([])
		alt(1,1)
		#cf_este3(["new mess",1,1])
		#cf_este3(["new mess",1,1])
		ctrl_f_escape_enter(["new message",1,1])
		
		#use_opera = "C:\\Program Files (x86)\\Opera\\launcher.exe"
		#subprocess.Popen([use_opera, file])
		#subprocess.Popen(['notepad.exe', "gen_emails.txt"])
		time.sleep(1)
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		af4(1,1)
		hod3(["ctrl","v",1,1])
		key([["tab",1,0,1]])
		wri("code.7z",1)
		htb("ctrl","shift","a",1,1)
		key([["enter",1,0,1]])
		file = "C:\\Users\\-\\Downloads\\code.7z"
		wri(file,2)
		#inc = cop([tex,inc])
		key([["enter",1,0,5]])
		#cf_este3(["send",1,1])
		ctrl_f_escape_enter(["send",1,1])

	input_gen_file =str(input("generate 7z file? 1 for yes, blank for no = "))
	input_email =str(input("email? 1 for yes, blank for no  = "))

	naw = []
	if input_gen_file=="1":
		generate_save_file(naw)
	if input_email=="1":
		email([])


inp = []
save(inp)