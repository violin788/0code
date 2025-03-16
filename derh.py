exec(open('util.py').read())
	
def derh(inp):
	import pyautogui
	today = datetime.date.today()
	friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
	fri2 = friday.strftime("%y%m%d")
	print (fri2)
	inp = []
	inp.append("symbol")
	inp.append("c for call, p for put")
	inp.append("price")
	inp = var(inp)
	print (inp)
	sym = inp[0]
	poc = inp[1]
	mat = ["c","p","C","P"]
	if poc not in mat:
		print("call or put has to be one of following, c,p,C,P, please put in again")
		poc =str(input("new value = "))
	poc = upp(poc)
	pri = inp[2]
	pri = str(pri)
	if "." in pri:
		pri = pri+"00"
	if "." not in pri:
		pri = pri+"000"	
	pri = pri.replace(".","")
	if len(pri)<8:
		for a in range(0,8-len(pri)):
			pri = "0"+pri
	sym = upp(sym)
	print (sym)
	#exp = "221007"
	exp = fri2
	spe = sym+exp+poc+pri
	#url = ["https://finance.yahoo.com/quote/"+spe+"?p="+spe]
	url = ["https://finance.yahoo.com/quote/"+spe+"/chart?p="+spe]
	url2 = "https://finance.yahoo.com/quote/"+sym+"/options?p=&straddle=true"	
	print (url)
	print (url2)
	num4([url,1])
inp = []
derh(inp)