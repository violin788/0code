exec(open('util.py').read())
def open(inp):
	#import subprocess,time
	to_open_with = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	what_to_open = "file:///C:/Users/--/code/open2.html"
	subprocess.Popen([to_open_with, "--incognito",what_to_open])
	time.sleep(2)
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","f4",1,1])
	#hold_button(["ctrl","f4",1,1])
	time.sleep(3)
	key([["esc",1,0,1]])
	import pyperclip
	#drive
	copy_paste2(["media788788"])
	key([["enter",1,0,4]])
	copy_paste2(["Medmed1!"])
	key([["enter",1,0,0]])

	
inp = []
open(inp)