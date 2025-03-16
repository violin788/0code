from tkinter import *
 
window = Tk()
window.title("Welcome to Dr.G app")
window.geometry('700x500')
window.configure(background = "#49a")
my_entries = []
def create_balanced_round_robin(players):
    """ Create a schedule for the players in the list and return it"""
    s = []
    if len(players) % 2 == 1: players = players + ["BYE"]
    # manipulate map (array of indexes for list) instead of list itself
    n = len(players)
    print(n)
    map = list(range(n))
    mid = n // 2
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = players[l1[j]]
            t2 = players[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                round.append((t2, t1))
            else:
                round.append((t1, t2))
 
        s.append(round)
        # rotate list by n/2, leaving last element at the end
        map = map[mid:-1] + map[:mid] + map[-1:]
    return s
 
def something():
    player_list = []
    entry_list = ""
    for entries in my_entries:
        if str(entries.get()) != "":
             player_list.append(str(entries.get()))
             entry_list = entry_list + str(entries.get()) + "\n"
#output
    entryvar = player_list
    #player_list.delete(1.0,tk.END)
   #player_list.insert(tk.END)
    my_label.config(text=entryvar)
    my_label.pack
 
    schedule = create_balanced_round_robin(player_list)
    my_label.config(text="\n".join(['{} vs. {}'.format(m[0], m[1]) for round in schedule for m in round]))
 
#Input
#row loop
for y in range(5):
     #column loopetes
     for x in range(5):
        my_entry = Entry(window)
        my_entry.grid(row=y, column=x, pady=20, padx=5)
        my_entries.append(my_entry)
my_button = Button(window, text="Click Me", command=something)
my_button.grid(row=6, column=0, pady=20)
my_label = Label(window,
                 text=" ",
                 font=("Arial Bold", 15))
my_label.grid(row=7, column=0, pady=20)
window.mainloop()