exec(open('util.py').read())
def mpc(inp):
	inp = inp
	from pydub import AudioSegment
	#importing file from location by giving its path
	fol = os.getcwd()+"\\mp3\\"
	fil = "tea"
	loc = fol+fil
	fir = loc+".mp3"
	print (fir)
	sound = AudioSegment.from_mp3(fir)
	sye()
	
	#Selecting Portion we want to cut
	StrtMin = 0
	StrtSec = 8
	EndMin = 0
	EndSec = 22
	# Time to milliseconds conversion
	StrtTime = StrtMin*60*1000+StrtSec*1000
	EndTime = StrtMin*60*1000+EndSec*1000
	# Opening file and extracting portion of it
	extract = sound[StrtTime:EndTime]
	# Saving file in required location
	out = fol+fil+"2"+".mp3"
	extract.export("/content/audio/new/"+out+".mp3", format="mp3")
	# new file portion.mp3 is saved at required location

inp = []
mpc(inp)