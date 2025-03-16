exec(open('util.py').read())
from tkinter import *
def gui(inp):
	
	#import tkinter
	import tkinter as tk
	master = Tk()
	master.title("GUI")
	master.geometry("200x120")
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
	mainloop()

inp = []
gui(inp)