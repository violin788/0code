exec(open('util.py').read())
from tkinter import *
def dev(inp):
	def run():
		run_file = symbol = file_to_test.get()
		if ".py" not in run_file:
			run_file = run_file+".py"
		exec(open(run_file).read())
	gui = Tk()
	gui.title("get stock info")
	gui.geometry("100x100")
	array = []
	array.append(["program to test"])
	"""
	array.append(["Start Date"])
	array.append(["End Date"])
	array.append(["Call or Put"])
	array.append(["Options Expiration"])
	"""
	for a,val in enumerate(array):
		Label(gui, text=val[0]).grid(row=a)
	row = -1
	file_to_test = Entry(gui)
	row = row+1
	file_to_test.grid(row=row,column=1)
	file_to_test.insert(0,"SPY")
	button_array = []
	button_array.append(["run",run])
	"""
	button_array.append(["gmail",gmail])
	button_array.append(["trading_view",trading_view])
	button_array.append(["unusal whales",unusal_whales])
	"""
	# Iterate over the labels and buttons
	for a,val in enumerate(button_array):
		button_name = val[0]
		#url = val[2]
		button = tk.Button(gui, text=button_name,command=val[1])
		row = row+1
		button.grid(row=row,column=0)
		#button.pack()






	mainloop()

inp = []
dev(inp)