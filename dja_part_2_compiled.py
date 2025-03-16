

#
def dja_part_2(inp):
	def load_data(inp):
		#data = load_data([load_file])
		load_file = inp[0]
		print("load_file = "+str(load_file))
		loaded_data = ""
		if ".xls" in load_file:
			import xlrd
			workbook = xlrd.open_workbook(load_file)
			sheet1 = workbook.sheet_by_index(0)	
			new_data = []
			for rowNumber in range(sheet1.nrows):
			    row = sheet1.row_values(rowNumber)
			    check = row[::-1]
			    new_row = []
			    for a,val in enumerate(check):
			    	if len(val)==0:
			    		continue
			    	new_row.append(val)
			    new_row = new_row[::-1]
			    new_data.append(new_row)
			loaded_data = new_data
		if ".csv" in load_file:
			def read_csv(inp):
				import csv
				file = inp[0]
				back = []
				with open(file, newline='') as f:
				    reader = csv.reader(f)
				    for row in reader:
				        #print(row)	
					    back.append(row)
				return back
			#file = load_file
			loaded_data = read_csv([load_file])
			#pri(back)
		if ".json" in load_file:
			with open(load_file, 'r') as f:
				loaded_data = json.load(f)
		if ".txt" in load_file or ".py" in load_file or ".js" in load_file or ".html" in load_file:
			text = open(load_file, "r")
			loaded_data = text.read()
		return loaded_data

	import os	

	load = load_data(["django_new.txt"])
	project_name = load[0:load.find("___")]
	url_name = load[load.find("___"):len(load)]
	url_name2 = url_name.replace("___","")
	print(load)
	#sye()
	command = "cd "+project_name
	#command = "start \"\" "+url
	os.system(command)	
	command = "py manage.py startapp "+url_name2
	#command = "start \"\" "+url
	os.system(command)
	
	
inp = []
dja_part_2(inp)