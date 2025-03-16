exec(open('util.py').read())
def open3(inp):
	
	import pyperclip

	to_open_with = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	what_to_open = "file:///C:/Users/--/code/open.html"
	
	subprocess.Popen([to_open_with, "--incognito",what_to_open])
	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","left",1,1])
	time.sleep(2)
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","f4",1,1])
	#hold_button(["ctrl","f4",1,1])
	time.sleep(2)
	key([["escape",1,0,1]])
	#key([["esc",1,0,1]])
	#drive
	copy_paste2(["media788788",1])
	key([["enter",1,0,4]])
	copy_paste2(["Medmed1!",1])
	key([["enter",1,0,0]])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["ctrl","pagedown",1,0])
	hold_button(["alt","d",1,1])
	copy_paste2(["gmail.com",1])
	key([["enter",1,0,0]])
	#hold_button(["ctrl","r",1,0])
	hold_button(["ctrl","pagedown",1,0])	
	copy_paste2(["violin78",0])
	key([["tab",1,0,0]])
	copy_paste2(["viovio",0])	
	key([["enter",1,0,0]])
	hold_button(["ctrl","pagedown",1,0])
	key([["tab",2,0,1]])
	copy_paste2(["savant78",0])
	key([["tab",1,0,1]])
	copy_paste2(["savant77",0])
	key([["enter",1,0,0]])
	hold_button(["ctrl","pagedown",1,1])
	hold_button(["ctrl","r",1,1])
	hold_button(["ctrl","pagedown",1,2])
	#key([["tab",3,0,1]])
	key([["tab",1,0,1]])		
	key([["tab",1,0,1]])		
	key([["tab",1,0,1]])		
	copy_paste2(["oversight333",0])
	key([["enter",1,0,2]])	
	copy_paste2(["Oveove1!",0])
	key([["enter",1,0,2]])	
	hold_button(["ctrl","pagedown",1,0])
	key([["tab",6,0,1]])
	copy_paste2(["violin78@protonmail.com",0])
	key([["tab",1,0,1]])	
	copy_paste2(["Viovio1!",0])
	key([["enter",1,0,0]])	

	#end()

	hold_2_buttons(["ctrl","shift","n",1,1])

	subprocess.Popen([to_open_with, "--incognito",what_to_open])
	time.sleep(2)
	key([["escape",1,0,1]])
	hold_button(["win","right",1,1])

	
inp = []
open3(inp)