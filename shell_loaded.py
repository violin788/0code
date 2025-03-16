exec(open('util.py').read())
def shell(inp):

	file_to_run = inp[0]
	command = ""
	if ".py" in file_to_run:
		command = "python "
	if ".py" in file_to_run:
		command = "node "
	command = command+file_to_run
	os.system(command)
