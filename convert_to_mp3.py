exec(open('util.py').read())
def mov(inp):
	fol = inp[0]
	lis = os.listdir(fol)
	for a in range(0,len(lis)):
		val = lis[a]
		#print (val)
		src = fol+val
		dst = ""

		if ".wav" in val:
			dst = src.replace("vio\\","vio\\1.5-wav\\")
			print(dst)
			#sys.exit()
			shutil.copy(src, dst)
			os.remove(src)
		if "2.mp3" in val:
			dst = src.replace("vio\\","vio\\1.5-mp3\\")
			shutil.copy(src, dst)
			os.remove(src)

		print(src)
		print(dst)
		"""
		shutil.copy(src, dst)
		os.remove(src)
		"""
		
			#src = 
			#print (val)
			#os.path.abspath("mydir/myfile.txt")
			#src = os.path.abspath(val)
			#print (src)
			#dst = src.replace("")
			#print (fol)

			#shutil.copy(src, dst)



	"""
	time.sleep(1)
	lis = os.listdir(loc)
	for a in range(0,len(lis)):
		val = lis[a]
		if fil in val:
		"""	

inp = []
mov(inp)