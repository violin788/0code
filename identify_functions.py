exec(open('util.py').read())
from tkinter import *
def tes(inp):

	text = load_data(["stock.py"])
	print(text)
	quit = 0
	loops = 0
	hits = []
	while(quit<1):
		if loops==0:
			iden = "("
			begin = 0
		find = 	text.find(iden,begin)
		if find<0:
			break
		string = text[find-50:find]
		reverse = string[::-1]
		if "\n" in reverse:
			new_line = reverse.find("\n")
			reverse2 = reverse[0:new_line]
			reverse2 = reverse2[::-1]
			reverse2 = reverse2.replace("\n","")
			string = reverse2
		if " " in string:
			reverse = string[::-1]
			reverse2 = reverse[0:reverse.find(" ")]
			string = reverse2[::-1]
		"""
		if "." in string:
			reverse = string[::-1]
			reverse2 = reverse[0:reverse.find(".")]
			string = reverse2[::-1]
		"""
		print(loops,find,string)
		begin = find+len(iden)
		loops = loops+1
		if string in hits:
			continue
		hits.append(string)

	count = 0
	skip = []
	skip.append("range")
	skip.append("Entry")
	skip.append("Button")
	skip.append("int")
	skip.append("enumerate")
	skip.append("append")
	skip.append("weekday")
	skip.append("strftime")
	skip.append("option_yahoo")
	skip.append("option_yahoo")
	skip.append("grid")
	skip.append("upper")	
	skip.append("stock_polygon")	
	skip.append("mainloop")	
	skip.append("get")	
	skip.append("get")
	skip.append(".insert")
	skip.append("gui.")
	skip.append("print")	
	for a,val in enumerate(hits):
		no = 0
		for b,valb in enumerate(skip):
			if valb in val:
				no = 1
				break
		if no==1:
			continue		
		count = count+1
		print(count,val)
	#file = 		
	

inp = []



tes(inp)