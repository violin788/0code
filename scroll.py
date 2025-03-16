exec(open('util.py').read())
exec(open('open_operations.py').read())

pri(storage)
#end()

#def scroll(inp):
	
import tkinter as tk
from tkinter import Scrollbar, Listbox

# Create the main Tkinter window
root = tk.Tk()
root.title("Scrollable List Example")

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Listbox widget and attach it to the scrollbar
listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Generate some example list items

#for i in range(1, 101):
for a,val in enumerate(storage):
	name = val[0]
	#listbox.insert(tk.END, f"Item {name}")
	listbox.insert(tk.END, name)

#for i in range(1, 101):
    #listbox.insert(tk.END, f"Item {i}")

# Configure the scrollbar to work with the Listbox
scrollbar.config(command=listbox.yview)

# Start the Tkinter main loop
root.mainloop()

	

#inp = []
#scroll(inp)