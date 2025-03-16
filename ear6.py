exec(open('util.py').read())
def ear5(inp):
	import requests	
	cwd = os.getcwd()
	fol = "ear"
	mkd([fol,cwd])
	#wen =int(input("week dow? = "))
	wen = 0
	from datetime import date
	now = date.today() 
	dow = now.weekday()
	print(now)
	print(dow)
	#mov = 7-day
	mon = now-datetime.timedelta(dow)
	mon2 = str(mon)
	dire = cwd+"\\"+fol
	lise = os.listdir(dire)
	fil1 = mon2+".txt"
	print(fil1)
	print(dire)
	out = dire+"\\"+fil1
	if fil1 not in lise:
		url = "https://www.investing.com/earnings-calendar/"
		num([url])
		time.sleep(3)
		key([["esc",1,0,1]])
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		tex = tki([])
		tex = str(tex)
		with open(out,"w",encoding="utf-8") as f:
		    f.write(tex)
	print(mon2+" = located")
	tex = rea([out])
	ray = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	mas = []
	for a,val in enumerate(ray):
		if a==len(ray)-1:
			break
		ide1 = val+", "
		spe = fin([tex,ide1,ray[a+1]])
		if len(spe)==0:
			continue
		lis = fin([spe,"\t","\n"])
		new = []
		new.append(["\n",""])
		new.append(["\t",""])
		lis2 = rep2([lis,new])
		for b,valb in enumerate(lis2):
			mas.append(valb)
	ide = []
	ide.append(["nam",0,"("])
	ide.append(["sym","(",")"])
	ide2 = []
	ide2.append(["cap/rev",0,"/"])
	mas2=[]
	for a,vala in enumerate(mas):
		ret = []
		for b,valb in enumerate(ide):
			cha = []
			cha.append([valb[1],""])
			cha.append([valb[2],""])
			bac = fin([vala,valb[1],valb[2]])
			bac2 = rep2([bac,cha])
			#print(a,b,bac2)
			ret.append(bac2)
		ret2 = [ret[1],ret[0]]
		ret = ret2
		val2 = vala[::-1]
		cha = []
		cha.append([" ","___"])
		cha.append(["______","___"])
		cha.append(["/___",""])
		cha.append(["___",","])
		for b,valb in enumerate(ide2):
			bac = fin([val2,valb[1],valb[2]])
			bac2 = bac[::-1]
			bac3 = rep2([bac2,cha])
			#las = bac3[len(bac3)-1:len(bac3)]
			rev = fin([bac3,0,","])
			rev = rev.replace(",","")
			if "-" in rev:
				rev = "---"
			cap = fin([bac3,",",","])
			try:
				cap = cap.replace(",","")
			except:
				naw="naw"
			rev = abb([rev])
			cap = abb([cap])
			ret2 = []
			ret2.append(cap)
			ret2.append(rev)
			ret2 = ret2+ret
		mas2.append(ret2)
	mas2.sort()
	hea = [["Cap","Rev","Sym","Name"]]
	mas3 = hea+mas2
	pri(mas3)
	mas4 = mas2[::-1]
	mas4 = hea+mas4
	nam = os.path.basename(__file__)
	nam = nam.replace(".py",".xls")
	wri2([nam,mas4])
	pri(mas4[0:20])
	#sw(nam,1)
	lis = mas4[0:20]
	lis2 = []
	for a,val in enumerate(lis):
		sym = val[2]
		lis2.append(sym+".json")
	pri(lis2)
	inf = os.listdir(dire)
	mis = che([inf,lis2])
	pri(mis)
	key = "FK98MBU38O64HAMH"
	for a,val in enumerate(mis):
		sym = val.replace(".json","")
		print(sym)
		url = "https://www.alphavantage.co/query?function=EARNINGS&symbol="+sym+ "&apikey="+key
		print (url)
		req = requests.get(url)
		data = req.json()
		sav = dire+"\\"+sym+".json"
		with open(sav, 'w') as f:
		    json.dump(data, f)
		sle([21])

	for a,val in enumerate(lis):
		sym = val[2]
		fil = "ear\\"+sym+".json"
		loa = js2([fil])
		que = loa["quarterlyEarnings"]
		for b,valb in enumerate(que):
			if b==10:
				break
			out = sym+"-"+str(b+1)+"-"+valb['reportedDate']
			print(out)

	mis = []
	ext = ".csv"
	print(lise)
	#sye()
	for a,val in enumerate(lis):
		sym = val[2]
		fil = sym+".his"+ext
		print(fil)
		if fil not in lise:
			mis.append(sym)
	print(mis)
	for a,val in enumerate(mis):
		sym = val
		if a==0:
			import yfinance as yf
		print (sym)
		inf = yf.Ticker(sym)
		#inc(["yfi"])
		#pro([get,a,sym])
		his = inf.history(period="5y")
		his = his[::-1]
		sav = dire+"\\"+sym+".his"+ext
		wri2([sav,his])
		print(his)
		sle([21])

		
inp = []
ear5(inp)