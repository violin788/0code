exec(open('util.py').read())
def cro(inp):
	
	import pygetwindow
	browser = pygetwindow.getWindowsWithTitle('chrome')[0] 
	browser.activate()
	browser.restore()
	sye()	
	hod3(["ctrl","t",1,1])
	#"http://croxyproxy.com/"
	wri("http://croxyproxy.com/",1)
	key([["enter",1,0,5]])
	import tkinter
	tkinfo = tkinter.Tk()
	#tex = tex.decode('utf8')
	#try:
	text = tkinfo.clipboard_get()
	hod3(["ctrl","v",1,1])
	key([["enter",1,0,0]])
	#print(text)
	
	"""
	url =str(input("nav? blank if def = "))
	if  ".com" not in url:
		url = url+".com"
	#if ".com" not in url:
		#url = "https://www.google.com/search?q="+url
	#print(url)
	#sye()
	#if nav=="":
	#	nav="www.google.com"
	#sch([3])
	#htb("ctrl","shift","n",1,1)
	alt(1,1)
	#af4(1,1)
	wri("croxyproxy.com",1)
	key([["enter",1,0,5]])
	wri(url,1)
	key([["enter",1,0,5]])
	"""



inp = []
cro(inp)