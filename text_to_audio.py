exec(open('util.py').read())
def ttf1(inp):

	import pyttsx3 
	file_name = "swiss"
	#file = name+".txt"
	text = rea5([file_name,"txt"])
	# Initialize the Pyttsx3 engine
	engine = pyttsx3.init()
	newVoiceRate = 120
	engine.setProperty('rate',newVoiceRate)
	title = "swiss"
	file = title+'.mp3'
	# We can use file extension as mp3 and wav, both will work
	engine.save_to_file(text, file)
	 
	# Wait until above command is not finished.
	engine.runAndWait()
	#sw(file,2)
	
inp = []
ttf1(inp)