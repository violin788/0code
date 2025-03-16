exec(open('util.py').read())

cwd = os.getcwd()
files = os.listdir(cwd)

libraries = []
for a,val in enumerate(files):
	if val[len(val)-3:len(val)]==".py":
	#if ".py" in val:
		try:
			text = load_data([val])
		except:
			print (val," = messed up")
			break
		quit = 0
		start_search_from = 0
		start_identifier = "import "
		end_identifier = "\n"
		values_found = []
		while(quit<1):
			start_point = text.find(start_identifier,start_search_from)
			if start_point<0:
				break
			end_point = text.find(end_identifier,start_point)
			found = text[start_point:end_point]
			values_found.append(found)
			if found not in libraries:
				libraries.append(found)
			start_search_from = end_point+len(end_identifier)
		pri(values_found)
pri(libraries)
command = "pip install"
for a,val in enumerate(libraries):
	if "*" in val:
		continue
	new = val.replace("import ","")
	new = new.replace(",","")
	if " as " in new:
		new = new[0:new.find(" as ")]
	print(new)
	run = "pip install "+val
	try:
		shell([run])
	except:
		continue
	#continue

	command = command+val.replace("import","")
print(command)

#pri(files)