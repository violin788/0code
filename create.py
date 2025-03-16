#exec(open('util.py').read())
def cre():
	import os,time
	nam =str(input("new file = "))
	fil = nam+".py"
	new = open(fil,"w")
	tex = "exec(open('util.py').read())\ndef "+nam+"(inp):\n\t"
	tex = tex+"\ninp = []\n"+nam+"(inp)"
	new.write(tex)
	new.close()
	os.startfile(fil)
	time.sleep(1)
	key([["down",2,0,0],["right",1,0,0]])
cre()