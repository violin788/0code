#exec(open('util.py').read())
import os,time,sys
import pyautogui
os.startfile("chrome.lnk")
time.sleep(5)
pyautogui.hotkey('alt', 'f4')

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
	copy_paste_enter("violin788788@gmail.com")
	pyautogui.press('enter')
	time.sleep(5)
	copy_paste_enter("Viovio1!")
	
	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(4)
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	copy_paste_enter("direct_measure")
	time.sleep(2)
	copy_paste_enter("votevote")

	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(1)
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	#pyautogui.press('tab')
	time.sleep(1)
	copy_paste("know357")
	pyautogui.press('tab')
	copy_paste_enter("know3333")
	pyautogui.press('enter')

	#facebook login
	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(1)
	copy_paste_tab("media788788@gmail.com",1)
	copy_paste_enter("Viovio2@")
	

	pyautogui.hotkey('ctrl', 'pageup')
	time.sleep(1)
	copy_paste_tab("violin78@protonmail.com",1)
	copy_paste("Viovio2@")
	pyautogui.press('enter')

	#https://www.tradingview.com/accounts/signin/
	#https://auth.openai.com/authorize?audience=https%3A%2F%2Fapi.openai.com%2Fv1&client_id=TdJIcbe16WoTHtN95nyywh5E4yOo6ItG&country_code=US&device_id=ac1ec193-016a-4a6d-83ee-d331db116a41&ext-login-allow-phone=true&ext-oai-did=ac1ec193-016a-4a6d-83ee-d331db116a41&ext-signup-allow-phone=true&prompt=login&redirect_uri=https%3A%2F%2Fchatgpt.com%2Fapi%2Fauth%2Fcallback%2Fopenai&response_type=code&scope=openid+email+profile+offline_access+model.request+model.read+organization.read+organization.write&screen_hint=login&state=Ds1yw0d-2H5xftgXS3rAtbxo9lLhBYqI0SsEZTswFrM&flow=treatment


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