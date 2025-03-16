exec(open('util.py').read())
def ear5(inp):
	import requests	
	cwd = os.getcwd()
	fol = "ear"
	dire = cwd+"\\"+fol
	lise = os.listdir(dire)
	mkd([fol,cwd])
	#wen =int(input("week dow? = "))
	wen = 0
	from datetime import date
	now = date.today() 
	dow = now.weekday()
	#print(now)
	#print(dow)
	#mov = 7-day
	mon = now-datetime.timedelta(dow)
	mon2 = str(mon)
	mon2 = "2023-07-31"
	#print(mon2)
	#sye()
	fil = mon2+".xls"
	lise = os.listdir(dire)
	if fil in lise:
		#print("already done")
		sye()
	fil1 = mon2+".txt"
	#print(fil1)
	#print(dire)
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
	#print(mon2+" = located")
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
			nam = ret[0]
			ret2 = ret2+ret
		if len(nam)>4:
			continue
		#if len(nam)<5:
			#print(nam,len(nam))
		mas2.append(ret2)
	#pri(mas2)
	#sye()
	mas2.sort()
	#pri(mas2)
	#sye()
	hea = [["Cap","Rev","Sym","Name"]]
	mas3 = hea+mas2
	#pri(mas3)
	mas4 = mas2[::-1]
	mas4 = hea+mas4
	nam = os.path.basename(__file__)
	nam = nam.replace(".py",".xls")
	wri2([nam,mas4])
	#pri(mas4[0:20])
	#sw(nam,1)
	lis = mas4[0:60]
	sto = lis
	#sto = mas4[0:20]
	sto2 = []
	for a,val in enumerate(sto):
		sym = val[2]
		sym2 = sym.upper()
		if sym==sym2:
			sto2.append(sym)
	lis2 = []
	for a,val in enumerate(sto):
		sym = val[2]
		lis2.append(sym+".json")
	nee = []
	ext = ".json"
	for a,val in enumerate(sto2):
		mor = val+ext
		nee.append(mor)
	mis = che([lise,nee])
	#print(mis)

	key = "FK98MBU38O64HAMH"
	for a,val in enumerate(mis):
		sym = val.replace(".json","")
		url = "https://www.alphavantage.co/query?function=EARNINGS&symbol="+sym+ "&apikey="+key
		print(a,len(mis),sym)
		print(url)
		req = requests.get(url)
		data = req.json()
		sav = dire+"\\"+sym+ext
		with open(sav, 'w') as f:
		    json.dump(data, f)
		sle([21])

	nee = []
	ext = ".his.csv"
	for a,val in enumerate(sto2):
		mor = val+ext
		nee.append(mor)
	mis = che([lise,nee])
	#print(mis)
	for a,val in enumerate(mis):
		sym = val[0:val.find(".")]
		if a==0:
			import yfinance as yf
		print(a,len(mis),sym)
		print("yfinance")
		inf = yf.Ticker(sym)
		#inc(["yfi"])
		#pro([get,a,sym])
		his = inf.history(period="5y")
		his = his[::-1]
		sav = dire+"\\"+sym+ext
		wri2([sav,his])
		#print(his)
		sle([21])

	nee = []
	ext = ".gen.xls"
	for a,val in enumerate(sto2):
		nee.append(val+ext)
	mis = che([lise,nee])
	#print(mis)
	ray = []
	for a,val in enumerate(sto2):
		sym = val
		fil = dire+"\\"+sym+".json"
		loa = js2([fil])
		#print(sym)
		#try:
		#pri(loa["quarterlyEarnings"])
		#try:
		print(sym)
		que = loa["quarterlyEarnings"]

		#except:
		#	continue
		#except:
		#	continue
		que2 = []
		for b,valb in enumerate(que):
			if b==10:
				break
			out = valb['reportedDate']
			que2.append(out)
		mor =[val]
		for b,valb in enumerate(que2):
			mor.append(valb)
		ray.append(mor)
	pri(ray)
	#pri(ray)
	out = dire+"\\"+"dat.xls"
	print(out)	
	wri2([out,ray])
	ski1 = 0
	for a,val in enumerate(sto2):
		#sym = val[0:val.find(".")]
		sym = val
		fil = "ear\\"+sym+".json"
		loa = js2([fil])
		que = loa["quarterlyEarnings"]
		que2 = []
		for b,valb in enumerate(que):
			if b==10:
				break
			#out = sym+"-"+str(b+1)+"-"+valb['reportedDate']
			out = valb['reportedDate']
			que2.append(out)
			#print(out)
		#print (sym,que2)
		fil = dire+"\\"+sym+".his.csv"
		loa = rea([fil])
		dat = []
		for b,valb in enumerate(loa):
			cor = valb[0]
			for c,valc in enumerate(que2):
				if valc in cor:
					mor = []
					mor.append(loa[b-1])
					mor.append(loa[b])
					mor.append(loa[b+1])
					dat.append(mor)
		for b,valb in enumerate(dat):
			for c,valc in enumerate(valb):
				try:
					valc[0] = valc[0][0:valc[0].find(" ")]
				except:
					continue
				try:
					for d in range(1,5):
						new = float(valc[d])
						new = new*100
						new  =int(new)
						new = float(new)
						new = new/100
						valc[d] = new
				except:
					continue
				valc[5] = int(valc[5])
				dat[b][c]=valc[0:6]
		hea = ["Date","Open","Low","High","Close","Volume"]
		for b,valb in enumerate(dat):
			for c,valc in enumerate(valb):
				#print(b,c,valc)
				#print("valb",valb)
				if c<len(valb):
					try:
						gap = float(valc[1])/float(valb[c+1][4])
					except:
						continue
					gap = dec([cha2([gap]),2])
					hig = hig = valc[2]/valc[1]
					hig = dec([cha2([hig]),2])
					low = low = valc[3]/valc[1]
					low = dec([cha2([low]),2])
					clo = clo = valc[4]/valc[1]
					clo = dec([cha2([clo]),2])
					#mor = [gap,hig,low,clo]
					mor = [gap,hig,low,clo]
					dat[b][c] = valc+mor
		#hea = ["Date","Open","Low","High","Close","Volume"]
		dat2 = []
		dat2.append(hea)
		#dat2 = hea
		for b,valb in enumerate(dat):
			dat2.append("")
			for c,valc in enumerate(valb):
				dat2.append(valc)
		dat = dat2
		sav = dire+"\\"+sym+ext
		#pri(dat)
		#sye()
		#print(sav)
		wri2([sav,dat])
	loc = dire+"\\"+"dat.xls"
	ead = rea([loc])
	pri(ead)
	#sye()
	#for a,val in enumerate(sto2):
		#sym = val[0:val.find(".")]
	out = []
	#pri(ead)
	for a,val in enumerate(sto):
		sym = val[2]
		print(sym,len(sym))
		for b,valb in enumerate(ead):
			sym2 = valb[0]
			#print("sym2",sym2)
			cor = ead[b][1:len(ead)]
			print(sym,sym2)
			if sym==sym2:
				print("match",sym,sym2)
				sav = dire+"\\"+sym+ext
				#try:
				his = rea([sav])
				spe = []
				spe2 = []
				sta = 0
				for c,valc in enumerate(his):
					if valc[0]=="":
						if sta==0:
							spe2 = []
							sta = 1
							continue
						if sta==1:
							spe.append(spe2)
							spe2 = []
					if valc[0]!="":
						spe2.append(valc)
				gap = []
				hig = []
				dow = []
				clo = []
				res = ""
				for c,valc in enumerate(spe):
					vol1 = valc[0][5]
					if "Volume" in vol1:
						continue
					vol1 = int(vol1)
					#vol1 = int(valc[0][5])
					print(vol1)
					vol2 = int(valc[1][5])
					vol3 = int(valc[2][5])
					if vol1>vol2:
						fir = valc[0]
						sec = valc[0]
					if vol2>vol1:
						fir = valc[1]
						sec = valc[2]
					gap1 = float(fir[6])
					hig1 = float(fir[7])
					dow1 = float(fir[8])
					clo1 = float(fir[9])
					res2 = ""
					if gap1>0:
						if abs(hig1)>abs(dow1):
							res2 = "C"
						if abs(dow1)>abs(hig1):
							res2 = "R"
					if gap1<0:
						if abs(dow1)>abs(hig1):
							res2 = "C"
						if abs(hig1)>abs(dow1):
							res2 = "R"
					res = res+res2
					gap.append(gap1)	
					hig.append(hig1)
					dow.append(dow1)
					clo.append(clo1)
				print(gap)
				print(hig)
				print(dow)
				print(clo)
				ab_gap = []
				for c,valc in enumerate(gap):
					new = [abs(valc),valc]
					ab_gap.append(new)
				ab_gap.sort()
				app = [sym,res,ab_gap[0]]
				out.append(app)
				print(res)
	#out.sort(key=lambda row: (row[2], row[3]), reverse=True)
	#out.sort(key=lambda : (col[1]))
	out.sort(key=lambda x:x[1],reverse=True)
		
	pri(out)
						
inp = []
ear5(inp)