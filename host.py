exec(open('util.py').read())
def host(inp):
	
	what_to_generate = []
	what_to_generate.append(["title","meow"])
	what_to_generate.append(["geometry","100x100"])
	what_to_generate.append(["function","server"])
	#what_to_generate.append(["button","start server","server"])
	gen_gui2([what_to_generate])

inp = []
host(inp)