exec(open('util.py').read())
def open5(inp):

	to_open_with = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	what_to_open = "file:///C:/Users/--/code/open.html"
	
	subprocess.Popen([to_open_with, "--incognito",what_to_open])
	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","left",1,1])

	hold_2_buttons(["ctrl","shift","n",1,1])

	subprocess.Popen([to_open_with, "--incognito",what_to_open])
	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","right",1,1])

	
inp = []
open5(inp)