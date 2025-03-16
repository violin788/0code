exec(open('util.py').read())
from tkinter import *
def web(inp):
	#import tkinter
	import tkinter as tk
	gui = Tk()
	gui.title("navigation")
	gui.geometry("80x200")
	array = []
	def rumble():
		url = "https://rumble.com/c/BannonsWarRoom"
		command = "start \"\" "+url
		os.system(command)
	def gmail():
		url = "https://gmail.com"
		command = "start \"\" "+url
		os.system(command)
	def trading_view():
		url = "https://www.tradingview.com/chart/?symbol=AMEX%3ASPY"
		command = "start \"\" "+url
		os.system(command)
	def unusal_whales():
		url = "https://unusualwhales.com/live-options-flow/free"
		command = "start \"\" "+url
		os.system(command)
	array.append(["rumble",rumble])
	array.append(["gmail",gmail])
	array.append(["trading_view",trading_view])
	array.append(["unusal whales",unusal_whales])
# Iterate over the labels and buttons
	for a,val in enumerate(array):
		button_name = val[0]
		#url = val[2]
		button = tk.Button(gui, text=button_name,command=val[1])
		button.pack()
		#button.grid(row=a, column=1, padx=10, pady=10)
		#button.pack()
	"""
	def rumble():
		url = "https://rumble.com/c/BannonsWarRoom"
		command = "start \"\" "+url
		os.system(command)
	rumble = Button(gui, text ="rumble", command = rumble)
	rumble.place(x=110,y=85)
	button.grid(row=i, column=1, padx=10, pady=10)
	"""
	"""
	button = tk.Button(window, text=buttons[i])

	# Use grid layout manager to align widgets in rows and columns
	label.grid(row=i, column=0, padx=10, pady=10)
	button.grid(row=i, column=1, padx=10, pady=10)
   """


	"""
	Label(master, text='Symbol').grid(row=0)
	Label(master, text='Date in Question').grid(row=1)
	Label(master, text='Call or Put').grid(row=2)
	Label(master, text='Override Expiration').grid(row=3)
	Label(master, text='Get info').grid(row=4)
	#def helloCallBack():
	#   msg=messagebox.showinfo( "Hello Python", "Hello World")
	def run_deriv():
		exec(open('deriv.py').read())
		deriv()
	   #msg=messagebox.showinfo( "Hello Python", "Hello World")
	#B = Button(master, text ="Get info", command = helloCallBack)
	B = Button(master, text ="Get info", command = run_deriv)
	B.place(x=110,y=85)
	e1 = Entry(master)
	e2 = Entry(master)
	e3 = Entry(master)
	e4 = Entry(master)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	#e4.grid(row=3, column=1)
	"""
	mainloop()
	
inp = []
web(inp)