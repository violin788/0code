import subprocess,pyperclip,time,pyautogui
# Path to the .exe file
exe_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
# Open the .exe file
subprocess.run([exe_path])
time.sleep(2)
# Copy text to clipboard
text_to_copy = "info33.pythonanywhere.com"
pyperclip.copy(text_to_copy)
# Paste text from clipboard
pasted_text = pyperclip.paste()
print(f"Pasted text: {pasted_text}")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter") 
pyautogui.hotkey("win", "left")
subprocess.run([exe_path])
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter") 
pyautogui.hotkey("win", "right")
pyautogui.hotkey("shift", "tab")
pyautogui.press("enter") 

text_to_copy = "media788788@gmail.com"
pyperclip.copy(text_to_copy)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter") 