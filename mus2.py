exec(open('util.py').read())
def mus2(inp):

	import musicalbeeps
	player = musicalbeeps.Player(volume = 0.3,
	                            mute_output = False)

	notes1 = ["C4","G4","G4","F4","E4","F4","E4","D4","D4","C4","D4","E4"]
	notes2 = ["D4","E4","F4","E4","C4","E4","D4","C4","G4","G4","F4","E4"]
	notes3 = ["F4","E4","D4","D4","C4","D4","E4","D4","E4","F4","E4","C4"]
	
	notes = notes1+notes2+notes3
	for a,val in enumerate(notes):
		#print(val)
		player.play_note(val,.3)	
inp = []
mus2(inp)