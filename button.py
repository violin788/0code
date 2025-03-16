exec(open('util.py').read())
def button(ray,between_wait,end_wait):
	for a in range(0,len(ray)):
		pyautogui.press(ray[a])
		time.sleep(between_wait)
	time.sleep(end_wait)


inp = []
button(inp)