exec(open('util.py').read())
def swi(inp):
	
	file1 =str(input("file1 = "))
	file2 =str(input("file2 = "))
	print("")
	print("to confirm")
	print("file1 = "+file1)
	print("file2 = "+file2)
	confirm =str(input("click to confirm"))
	confirm2 =str(input("this is the final confirm, after you click now it cannot be reversed, is this your final answer?!"))
	load1 = load_data([file1])
	load2 = load_data([file2])
	write_data([file2,load1])
	write_data([file1,load2])
	print("done")


inp = []
swi(inp)