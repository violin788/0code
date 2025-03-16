exec(open('util.py').read())
def cre():
	import os,time
	user_input =str(input("new file = "))
	save_file = user_input
	if ".py" not in user_input:
		save_file = save_file+".py"
	function_name = user_input
	if ".py" in user_input:
		function_name = function_name.replace(".py","")
	print("save file = "+save_file)
	print("function_name = "+function_name)
	text = ""
	text = text+"exec(open('util.py').read())\ndef "+function_name+"(inp):\n"
	text = text+"\t\n"
	text = text+"\t\n"
	text = text+"\t\n"
	text = text+"inp = []\n"
	text = text+function_name+"(inp)"
	new = open(save_file,"w")
	new.write(text)
	new.close()
	os.startfile(save_file)
	time.sleep(1)
	key([["down",3,0,0],["right",1,0,0]])
cre()