exec(open('util.py').read())
def compile2(inp):

	#python -m py_compile stock5.py
	file_name = "stock2"
	file_extension = ".py"
	load_file = file_name+file_extension
	if len(load_file)==0:
		load_file =str(input("file name = "))
	if ".py" not in load_file:
		load_file = load_file+".py"
	command = "python -m py_compile "+load_file
	os.system(command)
	folder = "C:\\Users\\-\\util\\__pycache__\\"
	file_to_open = folder+file_name+".cpython-37.pyc"
	#file_location = 
	sw2([file_to_open,0])

inp = []
compile2(inp)