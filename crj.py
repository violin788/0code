exec(open('util.py').read())
def crc():
	nam =str(input("new file = "))
	tex = rea4(["crj","txt"])
	#fil = nam
	ext = "java"
	wrt2([tex,nam,ext])
	ope = nam+"."+ext
	sw2([ope,1])
	"""
	new = open(fil,"w")
	tex = "exec(open('util.py').read())\ndef "+nam+"(inp):\n\t"
	tex = tex+"\ninp = []\n"+nam+"(inp)"
	new.write(tex)
	new.close()
	os.startfile(fil)
	time.sleep(1)
	key([["down",2,0,0],["right",1,0,0]])
	"""
crc()