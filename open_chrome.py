#exec(open('util.py').read())
def open_chrome(inp):
	def copy_paste(text):
		#copy_paste("test")
		pyperclip.copy(text)	
		pyautogui.hotkey('ctrl', 'v')
	def copy_paste_enter(text):
		#copy_paste_enter("test")
		pyperclip.copy(text)	
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press('enter')
	def copy_paste_tab(text,clicks):
		#copy_paste_tab("test",2)
		pyperclip.copy(text)	
		pyautogui.hotkey('ctrl', 'v')
		for a in range(0,clicks):
			pyautogui.press('tab')
	def esc_enter():
		#esc_enter()
		pyautogui.press('esc')
		pyautogui.press('enter')


	import pyperclip,pyautogui,subprocess,time
	url = "info44.pythonanywhere.com/"
	#text = "info44.pythonanywhere.com/"
	pyperclip.copy(url)	
	subprocess.run(["start", "chrome", "--incognito"], shell=True)
	time.sleep(1)
	pyautogui.hotkey('win', 'left')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'f')
	copy_paste("login pages")
	esc_enter()
	time.sleep(2)

	#copy_paste_tab("media788788@gmail.com",1)
	#copy_paste_enter("Medmed2@")

	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(2)
	copy_paste_enter("media788788@gmail.com")
	pyautogui.press('enter')
	time.sleep(5)
	copy_paste_enter("Medmed2@")
	
	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(4)
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	copy_paste_enter("ballotamend")
	time.sleep(2)
	copy_paste_enter("votevote")

	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(1)
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	time.sleep(1)
	copy_paste("know357")
	pyautogui.press('tab')
	copy_paste_enter("know3333")
	pyautogui.press('enter')

	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(1)
	copy_paste_tab("violin78@protonmail.com",1)
	copy_paste_enter("Viovio2@")
	

	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(1)
	copy_paste_tab("violin78@protonmail.com",1)
	copy_paste("Viovio2@")
	pyautogui.press('enter')


	#text = "info33.pythonanywhere.com/"
	pyperclip.copy(url)	
	subprocess.run(["start", "chrome", "--incognito"], shell=True)
	time.sleep(1)
	pyautogui.hotkey('win', 'right')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'f')
	copy_paste("already loaded")
	esc_enter()
	

	
inp = []
open_chrome(inp)