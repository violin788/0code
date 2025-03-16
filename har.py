exec(open('util.py').read())
def har(inp):
	def get_tab(inp):
		#ray = get_tab(inp):
		#ray = get_tab([name of txt file,format of file]]):
		#ray = get_tab(["mario",".txt"]]):	
		fil = inp[0]
		form = inp[1]
		fil = fil+"."+form
		text = rea([fil])
		#pri(text)
		back = nex4([text,"\n","\n"])
		for a,val in enumerate(back):
			back[a] = val.replace("\n","")
		pri(back)
		back2 = []
		for a,val in enumerate(back):
			new = []
			hyphen = 0
			for b,valb in enumerate(val):
				if hyphen==1:
					new.append("-"+valb)
					hyphen=0
					continue
				if "-" in valb:
					hyphen=1
					continue
				if hyphen==0:
					new.append(valb)
			#print(new)
			back2.append(new)
		#back2[0]=str(back2[0])
		title = ""
		for a,val in enumerate(back2[0]):
			title = title+val
		back2[0]=[title]
		pri(back2)
		#sye()
		return back2
	def transpose(inp):
		#final = transpose([inp])	
		#final = transpose([array to transpose])
		#final = transpose([back])
		back3 = inp[0]
		drop = "yes"
		#back2 = []
		if drop=="yes":
			back4 = []
			for a,val in enumerate(back3):
				if a==0:
					continue
				app = []
				for b,valb in enumerate(val):
					#print(a,b,valb)
					new = int(valb)
					if new<0:
						if new<-4:
							new = new+4
					if new>0:
						new = new-3
					app.append(new)
				back4.append(app)
		back4 = [[title]]+back4
		#pri(back4)
		return back4
	#nam = "sbc"
	#nam = "fur_elise"
	#nam = "ode_to_joy"
	#nam = "ekn"
	#nam = "jesus"
	nam = "nocturne"
	#nam = "air"
	#nam = "mario"
	#fil = nam+".txt"
	back = get_tab(["mario","txt"])
	pri(back)
	title = back[0]
	#back3 = back2[1:len(back)]
	#pri(back3)
	#sye()
	final = transpose([back])
	pri(final)	
	
inp = []
har(inp)