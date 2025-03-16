exec(open('util.py').read())
from tkinter import *
def run(inp):
	gui = Tk()
	gui.title("run")
	gui.geometry("250x300")

	array = []
	array.append(["program to run"])
	for a,val in enumerate(array):
		Label(gui, text=val[0]).grid(row=a)

	
	def gen_command():
		#gen_command([])
		#file = inputs[0]
		file_to_run = entry_file_to_run.get()
		exec(open(file_to_run).read())

	row = -1
	entry_file_to_run = Entry(gui)
	row = row+1
	entry_file_to_run.grid(row=row,column=1)
	entry_file_to_run.insert(0,"test.py")
	row = row+1
	button_run_file = Button(gui,text ="click to run file",command = gen_command)
	button_run_file.grid(row=row,column=0)


	
	#run_file = Button(gui,text ="run file",command = gen_command([]))
	#row = row+1





	mainloop()

	
inp = []
run(inp)