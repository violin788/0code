exec(open('util.py').read())
def swi(inp):
	cwd = os.getcwd()
	swi1 =str(input("switch 1 = "))
	swi2 =str(input("switch 2 = "))
	loa1 = rea4([swi1,"py"])
	loa2 = rea4([swi2,"py"])
	
	loa1 = loa1.replace("def "+swi1,"def "+swi2)
	loa1 = loa1.replace(swi1+"(inp)",swi2+"(inp)")

	loa2 = loa2.replace("def "+swi2,"def "+swi1)
	loa2 = loa2.replace(swi2+"(inp)",swi1+"(inp)")


	#tem1 = loa2.replace()
	#tem2 = loa1

	wrt([loa2,swi1,".py"])
	wrt([loa1,swi2,".py"])

	#make it so that there is a backup..no replace directly in case ram fail..
	
inp = []
swi(inp)