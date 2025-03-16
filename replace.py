exec(open('util.py').read())
def replace(inp):

	#cwd = os.getcwd()
	earn_lis = lis = os.listdir("earn")
	counter = 0
	for a,val in enumerate(earn_lis):
		if "yfinance_history" in val:
			counter = counter+1
			print(str(counter)+" "+val)
			src = "earn\\"+val
			dst = src.replace("yfinance_history","yfinance_history_original")
			shutil.copy(src,dst)
 
	#pri(earn_lis)
inp = []
replace(inp)