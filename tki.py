exec(open('util.py').read())
def tki(inp):
	import tkinter as tk
	tex = tk.Tk()
	#tex = tex.decode('utf8')
	try:
		tex2 = tex.clipboard_get()
	except:
		import win32clipboard
		#win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
		win32clipboard.OpenClipboard()
		tex2 = win32clipboard.GetClipboardData().encode('utf-8')
		tex2 = tex2.decode('utf8')
		win32clipboard.CloseClipboard()
	print (tex2)
	print (type(tex2))
	fil = "tki.txt"
	with open(fil, "w", encoding="utf-8") as f:
	    f.write(tex2)
	#wri2(["ear4.txt",tex])
	sw(fil,1)

		
inp = []
tki(inp)