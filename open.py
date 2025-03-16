exec(open('util.py').read())
exec(open('open_operations.py').read())
def open2(inp):
	import pyperclip
	#"chrome" or "firefox"
	#browser = "chrome"
	browser = "chrome"
	browser_index = ""
	if "chrome" in browser:
		browser_index = 2
	if "firefox" in browser:
		browser_index = 3

	inputs = whi("to open? just hit enter to open normal ones? = ")
	if len(inputs)==0:
		inputs = []
		inputs.append("gmail")
		inputs.append("drive")
		inputs.append("logins")	
		inputs.append("reddit_questions")
		inputs.append("keep")
		inputs.append("chatgpt")
		inputs.append("speechnotes")
		#inputs.append("reddit_notifications")
		inputs.append("reddit_new_notifications")
		inputs.append("reddit_old_notifications")
		inputs.append("twitter_login")
		inputs.append("messenger")
		inputs.append("protonmail")
		inputs.append("chatgpt")
		inputs.append("speechnotes")
	run = []
	for a in range(0,len(inputs)):
		val = inputs[a]
		#print("val",val)
		#continue
		#generate html file to open the next 6 urls?
		#if a==0 or a==6 or a==12:
		new_browser = 7
		#if a==0 or a==new_browser or a==new_browser*2:
		if a==0 or a==7 or a==14:	
			urls_to_load = []
			for b in range(0,6):
				try:
					to_load = inputs[a+b]
				except:
					continue
				for c in range(0,len(storage)):
					if storage[c][0]==to_load:
						urls_to_load.append(storage[c][1])
						break
			#html_file_to_open = "file:///C:/Users/--/code/html_to_open.html"
			html_file_to_generate = "html_to_open.html"
			what_to_open = "file:///C:/Users/--/code/"+html_file_to_generate
			if "chrome" in browser:
				run.append([gen_html,[urls_to_load,html_file_to_generate]])
			if "firefox" in browser:
				urls_to_load = urls_to_load[::-1]
				#urls_to_load.sort(key=lambda x: x[0], reverse=True)
				run.append([gen_html,[urls_to_load,html_file_to_generate]])
			to_open_with = ""
			#what_to_open = html_file_location
			if "chrome" in browser:
				to_open_with = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
				#what_to_open = "file:///C:/Users/-/code/open.html"
				#what_to_open = html_file_to_open
			if "firefox" in browser:
				to_open_with = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
				#skip = "skip"
			if a==0:
				run.append([subprocess_open,[5,what_to_open,to_open_with]])
			if a>0:
				if "chrome" in browser:			
					run.append([hold_2_buttons,["ctrl","shift","n",1,1]])
				if "firefox" in browser:			
					#run.append([hold_2_buttons,["ctrl","shift","n",1,1]])
					run.append([hold_button,["ctrl","n",1,1]])

				run.append([subprocess_open,[5,what_to_open,to_open_with]])
			if "chrome" in browser:
				if len(inputs)>8:
					run.append([hold_button,["ctrl","pagedown",1,1]])
					run.append([hold_button,["ctrl","f4",1,1]])
					if a>0:
						run.append([hold_button,["ctrl","f4",1,1]])
			if "firefox" in browser:
				run.append([hold_button,["ctrl","pageup",1,1]])
				run.append([hold_button,["ctrl","f4",1,1]])
			

		for b,valb in enumerate(storage):
			check = valb[0]
			if check==val:
				append_operations = valb[browser_index]
				for c,valc in enumerate(append_operations):
					run.append(valc)
				break	
		run.append([hold_button,["ctrl","pagedown",1,0]])
	pri(run)
	#end()
	for a,val in enumerate(run):
		function = val[0]
		inputs = val[1]
		function(inputs)

	
inp = []
open2(inp)