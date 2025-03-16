exec(open('util.py').read())
def gen_text(inp):

	base_text = """		<tr>
			<td><p id="0-0">0-0</p></td>
			<td><p id="0-1">0-1</p></td>
			<td><p id="0-2">0-2</p></td>
			<td><p id="0-3">0-3</p></td>
			<td><p id="0-4">0-4</p></td>
			<td><p id="0-5">0-5</p></td>
		</tr>"""
	print(base_text)
	for a in range(11,20):
		new = base_text.replace("0-",str(a)+"-")
		new = new.replace("\t\t","\t")
		print(new)
	
inp = []
gen_text(inp)