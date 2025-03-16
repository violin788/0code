#exec(open('har.py').read())
	
exec(open('util.py').read())
def mus(inp):
	#https://pypi.org/project/musicalbeeps/
	import musicalbeeps
	player = musicalbeeps.Player(volume = 0.3,
	                            mute_output = False)
	# Examples:
	# To play an A on default octave n°4 for 0.2 seconds
	#player.play_note("A5", 2)
	#player.play_note("A4", 2)

	repetoire = []
	repetoire.append([1,"C4"])
	repetoire.append([2,"E4"])
	repetoire.append([3,"G4"])
	repetoire.append([4,"C5"])
	repetoire.append([5,"E5"])
	repetoire.append([6,"G5"])
	repetoire.append([7,"C6"])
	repetoire.append([8,"E6"])
	repetoire.append([9,"G6"])
	repetoire.append([10,"C7"])
	repetoire.append([-1,"D4"])
	repetoire.append([-2,"G4"])
	repetoire.append([-3,"B4"])
	repetoire.append([-4,"D5"])
	repetoire.append([-5,"F5"])
	repetoire.append([-6,"A5"])
	repetoire.append([-7,"B5"])
	repetoire.append([-8,"D6"])
	repetoire.append([-9,"F6"])	
	repetoire.append([-10,"A6"])

	#nam = "sbc"
	#nam = "fur_elise"
	#nam = "ode_to_joy"
	#nam = "ekn"
	#nam = "jesus"
	#nam = "nocturne"
	#nam = "air"
	#nam = "mario"
	#nam = "prelude"
	#nam = "mozart1"
	
	nam = "top_gun2"	
	#fil = nam+".txt"
	
	#original_tabs = get_tab([nam,"txt"])
	original_tabs = rea4(["waltz","txt"])
	pri(original_tabs)
	#sye()
	convert = 0
	play = original_tabs
	if convert==1:
		#transposed_tabs = transpose([back,"down"])
		transposed_tabs = transpose([original_tabs,"down"])
		pri(transposed_tabs)
		play = transposed_tabs	
	#for a,val in enumerate(song_notes):
	#for a,val in enumerate(original_tabs):
	#"C4GGFEFEDDCDE"
	#notes = ["C4","G4","G4","F4","E4","F4","E4","D4","D4","C4","D4","E4"]
	for a,val in enumerate(play):
		if a==0:
			continue
		for b,valb in enumerate(val):
			tab = int(valb)
			note = ""
			for c,valc in enumerate(repetoire):
				if tab in valc:
					note = valc[1]
					break
			print(tab,note)	
			player.play_note(note,.3)	
	sye()
		
inp = []
mus(inp)