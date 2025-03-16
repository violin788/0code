exec(open('util.py').read())
def music(inp):

	songs = []
	songs.append(["V3","top_gun"])
	songs.append(["V0","prelude2"])
	songs.append(["V0","prelude5"])
	songs.append(["V0","waltz4"])
	songs.append(["V0","prelude2"])
	songs.append(["V5","beethoven"])
	songs.append(["V0","nocturne3"])
	songs.append(["V3","waltz5"])
	songs.append(["V1","take"])
	songs.append(["V0","serenade"])
	songs.append(["V0","yankee"])
	#songs.append(["V6","waltz6"])
	songs.append(["V1","waltz6"])
	songs.append(["V8","swift1"])
	songs.append(["V0","god_save"])
	songs.append(["V0","america"])

	#for move_octave, 1 for up 1 octave,-1 for down..0 forsame
	title = "america"
	move_octave = 1
	sound_length = .3
	line_length = 3

	track_to_get = get_track([title,songs])
	print (track_to_get)

	text = rea5([title,"gro"])
	print(text)
	notes = nex4([text,"\n","\n"])
	notes2 = []
	for a,val in enumerate(notes):
		val = val.replace("\n","")
		if "T0.0000" not in val:
			if track_to_get in val:
				notes2.append(val)
	pri(notes2)
	notes3 = []
	for a,val in enumerate(notes2):
		for b,valb in enumerate(keys):
			check = valb[0]
			if check in val:
				correct = valb[1]
				notes3.append(correct)
	pri(notes3)
	#for move_octave, 1 for up 1 octave,-1 for down..0 forsame
	#move_octave = 1
	#move_octave = 0
	nums = ["0","1","2","3","4","5","6","7","8","9",]
	for a,val in enumerate(notes3):
		for b,valb in enumerate(nums):
			if valb in val:
				change = str(int(valb)+move_octave)
				#val.replace(valb,change)
				notes3[a]=val.replace(valb,change)
	pri(notes3)
	#sye()
	text = ""
	counter = 0
	add = ""
	for a,val in enumerate(notes3):
		counter = counter+1
		text = text+str(val)+" "
		if counter==line_length:
			text = text+"\n"
			counter=0
	file_name = title
	extension = ".txt"
	text = file_name+"\n"+text
	print(text)
	wri2([file_name+extension,text])
	sw(file_name+".txt",2)

	import musicalbeeps
	player = musicalbeeps.Player(volume = 0.3,
	                            mute_output = False)
	harmonica_notes = []
	for a,val in enumerate(notes3):
		match = 0
		for b,valb in enumerate(repetoire):
			if val in valb:
				print(val,valb)
				harmonica_notes.append(valb[0])
				match=1
				break
		if match==0:
			harmonica_notes.append(val)
	pri(harmonica_notes)
	#sye()
	harmonica2 = []
	counter = 0
	append = []
	for a,val in enumerate(harmonica_notes):
		counter = counter+1
		append.append(val)
		if a==len(harmonica_notes)-1:
			harmonica2.append(append)
		if counter==line_length:
			harmonica2.append(append)
			counter=0
			append = []
	harmonica_text = ""+title+"\n"
	for a,val in enumerate(harmonica2):
		harmonica_text = harmonica_text+str(val)+"\n"
	pri(harmonica2)
	save = title+"-harmonica"+".txt"
	wri2([save,harmonica_text])
	sw(save,2)
	#notes4 = 


	#sye()
	#for a,val in enumerate(harmonica_notes):
	#	player.play_note(val,.3)

	for a,val in enumerate(notes3):
		player.play_note(val,sound_length)
	# Examples:
	
	
	#"T0.0000"
	#pri(notes)
	
inp = []
music(inp)