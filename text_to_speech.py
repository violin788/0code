exec(open('util.py').read())
def tts1(inp):
	import pyttsx3
	engine = pyttsx3.init()
	newVoiceRate = 120
	engine.setProperty('rate',newVoiceRate)
	name = "twitter"
	#file = name+".txt"
	text = rea5([name,"txt"])
	#begin = text.find("Elect Policies, Abolish Politicians")
	#text2 = text[begin:len(text)]
	#text =text2
	#print(text)
	#sye()

	#text = "haha haha haha haha "
	engine.say(text)
	#engine.say("I will speak this text")
	engine.runAndWait()
	
inp = []
tts1(inp)