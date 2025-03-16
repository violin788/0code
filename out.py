exec(open('util.py').read())
def out(inp):
	from gtts import gTTS
	import os,time
	from datetime import datetime
	#tex = 'yo yo yo sup sup yo yo!'
	tex = rea(["pdf2.txt"])
	le = len(tex)
	est = int(le/100)
	est2 = ""
	if est>60:
		est = est/60
		est2 = str(est)+" minutes"
	if "min" not in est2:
		est2 = str(est)+" seconds"	
	print (tex)
	print(str(le)+" = length in characters")
	print("-----------------------")
	print(est2+" = estimated time to generate")
	print("-----------------------")
	print("approx 100 characters per second generated")
	tim1 = time.time()
	rea1 = datetime.fromtimestamp(tim1)
	print("start time = "+str(rea1))
	language = 'en'
	myobj = gTTS(text=tex, lang=language, slow=False)
	myobj.save("out.mp3")
	tim2 = time.time()
	print(tim2)
	dif = int(tim2-tim1)
	div = float(le)/float(dif)
	print(str(dif)+" seconds = time to generate")
	print(str(div)+" characters per second = mp3 generate rate")
	os.system("out.mp3")
	
inp = []
out(inp)