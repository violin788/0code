exec(open('util.py').read())
def play(inp):

	import musicalbeeps
	player = musicalbeeps.Player(volume = 0.3,
	                            mute_output = False)

	#title = "top_gun"
	#title = "take2"
	title = "god_save"
	sound_length = .3
	text = rea5([title,"txt"])
	notes = nex4([text,"\n","\n"])
	for a,val in enumerate(notes):
		notes[a]=val.replace("\n","")
	#notes2 = nex4([notes," "," "])
	notes2 = []
	for a,val in enumerate(notes):
		append = nex4([val," "," "])
		notes2.append(append)
	pri(notes2)
	notes3 = []
	for a,val in enumerate(notes2):
		for b,valb in enumerate(val):
			valb2 = valb.replace(" ","")
			if len(valb2)>0:
				notes3.append(valb2)
	pri(notes3)
	#sye()
	harmonica_tabs = []
	#counter = -1
	append = []
	for a,val in enumerate(notes3):
		#counter = counter+1
		for b,valb in enumerate(repetoire):
			if val in valb:
				append.append(valb[0])
				break
		if len(append)==5:
			harmonica_tabs.append(append)
			append = []
	pri(harmonica_tabs)
	save_name = title+"-harmonica"
	wri5([save_name,".txt",str(harmonica_tabs)])
	sw(save_name+".txt",2)

	for a,val in enumerate(notes3):
		#skip title line..
		#if a==0:
		#	continue
		print(val)
		player.play_note(val,sound_length)



inp = []
play(inp)