exec(open('util.py').read())
exec(open('open_operations.py').read())
#def scroll2(inp):
	
import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, Button

# Function to handle search
def search():
    query = entry.get().strip().lower()  # Get the search query and convert to lowercase
    listbox.delete(0, tk.END)  # Clear current items in the listbox
    # Filter and insert items matching the query
    for item in storage:
        #if query in item.lower():
        if query in item[0]:
            listbox.insert(tk.END, item)

# Sample data
"""
all_items = [
    "Apple",
    "Banana",
    "Cherry",
    "Durian",
    "Elderberry",
    "Fig",
    "Grape",
    "Honeydew",
    "Kiwi",
    "Lemon",
    "Mango",
    "Orange",
    "Papaya",
    "Quince",
    "Raspberry",
    "Strawberry",
    "Tangerine",
    "Ugli fruit",
    "Watermelon"
]
"""

# Create the main Tkinter window
root = tk.Tk()
root.title("Search Bar Example")

# Create a frame for search bar and listbox
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a search bar (Entry widget)
entry = Entry(frame, width=30, font=("Helvetica", 12))
entry.grid(row=0, column=0, padx=10)

# Create a search button
search_button = Button(frame, text="Search", command=search)
search_button.grid(row=0, column=1, padx=10)

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Listbox widget
listbox = Listbox(root, yscrollcommand=scrollbar.set, width=50, height=15, font=("Helvetica", 12))
listbox.pack(pady=10)

# Insert all items into the Listbox initially
for item in storage:
    listbox.insert(tk.END, item[0],item[1],"")

# Configure the scrollbar to work with the Listbox
scrollbar.config(command=listbox.yview)

# Start the Tkinter main loop
root.mainloop()
	
	
#inp = []
#scroll2(inp)