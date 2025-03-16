exec(open('util.py').read())
def mus3(inp):
	import musicalbeeps
	player = musicalbeeps.Player(volume = 0.3,
	                            mute_output = False)

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
	"""
	notes1 = ["C5","G5","G5","F5","E5","F5","E5","D5","D5","C5","D5","E5"]
	notes2 = ["D5","E5","F5","E5","C5","E5","D5","C5","G5","G5","F5","E5"]
	notes3 = ["F5","E5","D5","D5","C5","D5","E5","D5","E5","F5","E5","C5"]
	notes = notes1+notes2+notes3
	"""
	notes = ["F4","G4","A5","B5","C5","D5","B5","D5","C5"]
	final = ""
	for a,val in enumerate(notes):
		for b,valb in enumerate(repetoire):
			if val in valb:
				final = final+" "+str(valb[0])
	print(final)


	for a,val in enumerate(notes):
		player.play_note(val,.3)	
		"""
		print(val[0])
		player.play_note(val[1], .3)
		print(repetoire[a+10][0])
		player.play_note(repetoire[a+10][1], .3)
		"""	


inp = []
mus3(inp)