exec(open('util.py').read())
def compile(inp):

	main_file = "conemu_start.py"
	files_to_compile = []
	files_to_compile.append("util")
	#files_to_compile.append("nav2")
	files_to_compile.append(main_file)
	for a,val in enumerate(files_to_compile):
		if ".py" not in val:
			files_to_compile[a] =val+".py"
	#pri(files_to_compile)
	new_file_text = ""
	for a,val in enumerate(files_to_compile):
		text =load_data([val])
		new_file_text = new_file_text+"\n\n"+text
	new_file_text = new_file_text.replace("exec(open('util.py').read())","")
	out_name = main_file+"_compiled"
	out_file = out_name+".py"	
	wri2([out_file,new_file_text])
	command = "python -m py_compile "+out_file
	os.system(command)
	file_to_open = "C:\\Users\\-\\code\\__pycache__\\"+main_file+"_compiled.cpython-37.pyc"
	open_py_cache="C:\\Users\\--\\code\\__pycache__"
	sw2([open_py_cache,0])




	
inp = []
compile(inp)