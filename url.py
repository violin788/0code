exec(open('util.py').read())
def url(inp):

	name =str(input("title of new url = "))
	url2 =str(input("url of new url = "))

	text = load_data(["stock.py"])
	#print(text)
	before = "url_array = []"
	function = "def"

	print("")
	fun1 = "def ___title_name___():\n"
	fun2 = "\turl = \"___url___\"\n"
	fun3 = "\tcommand = \"start \\"\" \"+url\n"
	fun4 = "\tos.system(command)"
	fun = fun1+fun2+fun3+fun4
	fun = fun.replace("___title_name___",name)
	fun = fun.replace("___url___",url2)

	print(fun)
	sye()


	after = ""
	text.replace(before,after)
	print(text)
	
inp = []
url(inp)