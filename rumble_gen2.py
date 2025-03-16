exec(open('util.py').read())
def rumble_gen2(inp):
	documentation = []

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__person_position__")
	new.append("__description__")
	new.append("__embed_url__")
	new.append("__rumble_url__")
	documentation.append(new)
	new = []
	new.append("arizona")
	new.append("lankford")
	new.append("us senator")
	new.append("130 thousand illegal votes were cast in Nevada")
	new.append("https://rumble.com/embed/v4spnbx/?pub=3i4h9q")
	new.append("https://rumble.com/v4v6n4l-nevada-130-thousand-illegal-votes-were-cast-in-nevada.html")
	documentation.append(new)
	new = []
	new.append("michigan")
	new.append("Jim Runestad")
	new.append("(R) Michigan State Senator")
	new.append("Explanation of Voter Michigan Fraud")
	new.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	new.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	documentation.append(new)
	new = []
	new.append("arizona")
	new.append("??")
	new.append("??")
	new.append("Explanation of Voter Fraud")
	new.append("https://rumble.com/embed/v4qvth5/?pub=3i4h9q")
	new.append("https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html")
	documentation.append(new)
	new = []
	new.append("georgia")
	new.append("??")
	new.append("??")
	new.append("Over 300,000 ballot images lost Georgia 2020 recount (Fulton county)")
	new.append("https://rumble.com/embed/v4rayvc/?pub=3i4h9q")
	new.append("https://rumble.com/v4tst7l-over-300000-ballot-images-lost-georgia-2020-recount-fulton-county.html")
	documentation.append(new)
	new = []
	new.append("georgia")
	new.append("Joseph Rossi")
	new.append("??")
	new.append("Georgia Recount Violated Georgia Election Law")
	new.append("https://rumble.com/embed/v4r928i/?pub=3i4h9q")
	new.append("https://rumble.com/v4tqwl6-georgia-joseph-rossi-georgia-recount-violated-georgia-election-law.html")
	documentation.append(new)
	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__person_position__")
	new.append("__description__")
	new.append("__embed_url__")
	new.append("__rumble_url__")
	documentation.append(new)

	documentation2 = []
	for a,val in enumerate(documentation):
		state_check = val[0]
		if "__state__" in state_check:
			continue
		match = 0
		for b in range(0,len(documentation2)):
			valb = documentation2[b]
			state_check2 = valb[0]
			if state_check==state_check2: 
				match = 1
				documentation2[b].append(val)
				break
		if match==0:
			documentation2.append([state_check,val])

	pri(documentation2)
	#end()
	final_html = "<html><body id=\"body_main\">\n"
	style = "<style>\n"
	apos = "\""		
	def gen(inputs):
		#code = div(["div","arizona-1","gjs-grid-row"])
		element = inputs[0]
		iden = inputs[1]
		clas = inputs[2]
		text = "<"+element+" class=\""+clas+"\" id=\""+iden+"\">\n"
		return text
	for a,val in enumerate(documentation2):
		row = 1
		col = 1
		state = val[0]
		final_html = final_html+gen(["div",state+"-row-"+str(row),"gjs-grid-row"])
		final_html = final_html+gen(["div",state+"-col-"+str(col),"gjs-grid-column"])
		final_html = final_html+gen(["div",state+"-title-row"+str(row),"gjs-grid-row"])
		final_html = final_html+gen(["div",state+"-title-col"+str(col),"gjs-grid-column"])
		#final_html = final_html+gen(["div",state+"-eh","gjs-grid-column"])
		final_html = final_html+"<div>"+state+"</div></div></div></div>\n"
		#final_html = final_html+gen(["div",state+"-row2-"+str(row),"gjs-grid-row"])
		#col = col+1
		#final_html = final_html+gen(["div",state+"-col-"+str(col),"gjs-grid-column"])
		for b in range(1,len(val)):
			valb = val[b]
			try:
				embed_url= valb[4]
			except:
				continue
			iframe_id = state+str(b)
			col = col+1
			if b==1:
			#final_html = final_html+gen(["div",state+"-col-"+str(col),"gjs-grid-column"])
				final_html = final_html+gen(["div",state+"-col-"+str(col),"gjs-grid-column"])
				final_html = final_html+gen(["div",state+"-media-row-"+str(row),"gjs-grid-row"])
			final_html = final_html+gen(["div",state+"-col-media-"+str(col),"gjs-grid-column"])
			final_html = final_html+"<iframe id=\""+iframe_id+"\" src=\""+embed_url+"\"></iframe>\n"
			final_html = final_html+"</div>"
			style = style+"\n#"+iframe_id+" {width: 400px;height: 300px;}"
		final_html = final_html+state+"</div></div></div>\n"
	style =style+"\n</style>"
	final_html = final_html+"</body>\n"+style
	final_html = final_html
	final_html = final_html+"\n</html>"
	print(final_html)
	out_file = "election5.html"
	write_data([out_file,final_html])
	chrome_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	file = "file:///C:/Users/--/code/"+out_file
	source = "view-source:file:///C:/Users/--/code/"+out_file	
	subprocess.Popen([chrome_location, file])
	time.sleep(1)
	hold_button(["ctrl","u",1,1])
	#subprocess.Popen([chrome_location, source])


inp = []
rumble_gen2(inp)