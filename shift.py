exec(open('util.py').read())
def shift(inp):

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
	#for move_octave, 1 for up 1 octave,-1 for down..0 forsame
	title = "serenade"
	#move_octave = 1
	sound_length = .3
	track_to_get = get_track([title,songs])


	#track_to_get = "V0"
	#for move_octave, 1 for up 1 octave,-1 for down..0 forsame
	move_octave = 1
	sound_length = .4
	text = rea5([title,"gro"])
	print(text)
	notes = nex4([text,"\n","\n"])
	notes2 = []
	for a,val in enumerate(notes):
		val = val.replace("\n","")
		if "T0.0000" not in val:
			if track_to_get in val:
				notes2.append(val)
	#pri(notes2)	
	notes3 = []	
	for a,val in enumerate(notes2):
		for b,valb in enumerate(keys):
			check = valb[0]
			if check in val:
				correct = valb[1]
				notes3.append(correct)
	#pri(notes3)

	sharp_or_flat = 0
	for a,val in enumerate(notes3):
		if "#" in val:
			sharp_or_flat = 1
			break
	#pri(notes3)
	if sharp_or_flat==1:
		for a in range(1,12):
			notes4 = []
			for b in range(0,len(notes3)):
				specific = notes3[b]
				match = -1
				for c,valc in enumerate(keys):
					if notes3[b] in valc:
						match = c
				#index = keys.index(notes3[b])
				index = match 
				print("index",index)
				print(keys[index+a])
				new = keys[index+a][1]
				#index = notes3.index(valb)+a
				print(index)
				#try:
				notes4.append(new)
				#except:
					#continue
			redo = 0
			#pri(notes4)
			for b,valb in enumerate(notes4):
				if "#" in valb:
					redo = 1
					break
			print("redo",redo)
			if redo==0:
				print(a)
				print("success")
				pri(notes4)
				sye()
				import musicalbeeps
				player = musicalbeeps.Player(volume = 0.3,
				                            mute_output = False)
				for a,val in enumerate(notes4):
					note = val[1]
					print(note)
					player.play_note(note,.3)
				break
			if a==11 and redo==1:
				print ("total failure..")



	
inp = []
shift(inp)