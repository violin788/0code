exec(open('util.py').read())
def scr(inp):
	
	tex = "put cursor at start position, click enter"
	inp =str(input(tex))
	#alt(1,1)
	loc1 = pyautogui.position()
	#print(loc1)
	tex = "put cursor at end position, click enter"
	inp =str(input(tex))
	loc2 = pyautogui.position()
	print(loc1,loc2)
	#you have to click, ctrl+fn+home
	#htb("ctrl","function","home",1,2)
	alt(1,1)
	pyautogui.hotkey('ctrl','fn','prtsc')
	time.sleep(1)
	pyautogui.moveTo(loc1)
	pyautogui.mouseDown()
	pyautogui.moveTo(loc2)
	pyautogui.mouseUp()
	
	
	sye()
	
	

inp = []
scr(inp)