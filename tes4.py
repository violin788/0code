exec(open('util.py').read())

alt_win81(["Sublime",2])

number_of_clicks = 50

for a in range(0,number_of_clicks):
	hold_button(["ctrl","f4",1,0])
	key([["n",1,0,0]])
