exec(open('util.py').read())
def conv(inp):
	
	from os import path
	from pydub import AudioSegment

	loc = inp[0]
	fil = inp[1]
	typ = "mp3"

	src = loc+fil+"."+typ

	typo = "wav"
	dst = loc+fil+"."+typo
	sound = AudioSegment.from_mp3(src)
	sound.export(dst, format="wav")
	time.sleep(2)


	lis = os.listdir(loc)

	#fil = "Air_12-20_Air On The G String, J. S. Bach - Anastasiya Petryshak, Violin"

	fil = fil[0:len(fil)-1]

	for a in range(0,len(lis)):
		val = lis[a]
		if fil in val:
			print (val)
			src = loc+val
			dst = loc+"vio\\"+val
			print ("src",src)
			print ("dst",dst)

			shutil.copy(src, dst)
			os.remove(src)

inp = []
conv(inp)