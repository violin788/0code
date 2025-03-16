exec(open('util.py').read())
from tkinter import *
def run_gui(inp):
	import tkinter as tk
	run = Tk()
	run.title("meow")
	Label(run, text="python file").grid(row=0,column=0)
	new_entry = Entry(run)
	new_entry.grid(row=0,column=1)
	button_run_file = Button(run,text ="run python file")
	button_run_file.grid(row=0,column=2)
	Label(run, text="javascript file").grid(row=1,column=0)
	new_entry = Entry(run)
	new_entry.grid(row=1,column=1)
	button_run_file = Button(run,text ="run javascript file")
	button_run_file.grid(row=1,column=2)
	mainloop()
inp = []
run_gui(inp)