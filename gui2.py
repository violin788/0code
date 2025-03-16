exec(open('util.py').read())
from tkinter import *

def gui2(inp):
	
	from tkinter import messagebox
	master = Tk()
	master.geometry("100x100")
	def helloCallBack():
	   msg=messagebox.showinfo( "Hello Python", "Hello World")
	B = Button(master, text ="Hello", command = helloCallBack)
	B.place(x=50,y=50)
	master.mainloop()

inp = []
gui2(inp)