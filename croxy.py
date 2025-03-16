exec(open('util.py').read())
def croxy(inp):
	
	navigate =str(input("where to nagivate?"))
	if "www" not in navigate:
		navigate = "www."+navigate
	if ".com" not in navigate:
		navigate = navigate+".com"


	alt_win81(["Chrome",1])	
	hold_button(["ctrl","t",1,1])
	copy_paste2(["croxyproxy.com",1])
	key([["enter",1,0,5]])
	copy_paste2([navigate,1])
	key([["enter",1,0,0]])


	
inp = []
croxy(inp)