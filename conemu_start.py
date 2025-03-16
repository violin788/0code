#exec(open('util.py').read())
def startup(inp):

	import os,pyautogui,time

	def hold_button(inp):
		#hold_button(["ctrl","pagedown",1,1])
		first = inp[0]
		second = inp[1]
		clicks = inp[2]
		wait = inp[3]
		pyautogui.keyDown(first)
		for a in range(0,clicks):
			pyautogui.press(second)
		pyautogui.keyUp(first)
		time.sleep(wait) 

	def copy_paste2(inp):
		#copy_paste2(["paperclip",2])
		import pyperclip
		#copy_paste(["paperclip"])
		wait_time = inp[1]
		text_to_copy_paste = inp[0]
		pyperclip.copy(text_to_copy_paste)
		hold_button(["ctrl","v",1,0])
		time.sleep(wait_time)

	file = "C:\\Program Files\\ConEmu\\ConEmu64.exe"
	os.startfile(file)
	nav_to = "C:\\Users\\-\\code"
	command = "cd "+nav_to
	os.system(command)
	time.sleep(2)
	#command = "python open.py"
	#os.system(command)
	copy_paste2(["python open.py",2])
	time.sleep(2)
	pyautogui.press("enter")




inp = []
startup(inp)