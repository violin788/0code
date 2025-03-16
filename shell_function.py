exec(open('util.py').read())
def shell(inp):
	file_to_run = inp[0]
	command = ""
	if ".py" in file_to_run:
		command = "python "
	if ".js" in file_to_run:
		command = "node "
	if "." not in file_to_run:
		print("you have to put .py or .js on it")
	if "." in file_to_run:	
		command = command+file_to_run
		os.system(command)

