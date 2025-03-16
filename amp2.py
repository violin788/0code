exec(open('util.py').read())
def amp2(inp):
	from pydub import AudioSegment
	
	loc = inp[0]
	fil = inp[1]

	#loc = "C:\\Users\\-\\Downloads\\y\\"
	#fil =str(input("file = "))
	lis = os.listdir(loc)
	print (lis)	
	mat = []
	las = []
	for a in range(0,len(lis)):
		val = lis[a]
		val = val.replace(".mp3","")
		val = val.replace(".wav","")
		if fil in val:
			mat.append(val)
			try:
				num = int(val[len(val)-1:len(val)])
			except:
				continue
			las.append(num)
	print (mat)
	las.sort()
	print (las)
	if len(las)>0:
		nex = str(las[0]+1)
	if len(las)==0:
		nex = "2"
	#sys.exit()
	fil = loc+fil
	typ = "mp3"
	inp = fil+"."+typ
	#inp = fil+".mp3"
	song = AudioSegment.from_mp3(inp)
	loudness = song.dBFS
	print (loudness)
	#sys.exit()
	dif =abs(float(loudness))
	dif = dif/2 
	louder_song = song+dif
	out = fil+nex+"."+typ
	louder_song.export(out, format=typ)
inp = []
amp2(inp)