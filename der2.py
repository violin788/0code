exec(open('util.py').read())
def der2(inp):
	from datetime import date
	now = date.today() 
	now2 = now.strftime('%m/%d/%Y')
	now3 = datetime.datetime.strptime(now2,'%m/%d/%Y')
	#os.path.getctime('file_path')
	tim = datetime.datetime.now()
	"""
	stock = "---"
	tim2 = "---"
	go = "---"
	"""
	"""
	#USO.0opt.11,45--03.17
	stock = "USO"
	tim2 = "11,45--03.17"
	go = ""
	"""
	day = now.weekday()
	#day = 5
	cha = 0
	if day<4:
		cha = 4-day
	if day>4:
		cha = 7-(day-4)
	fri = now+datetime.timedelta(cha)
	fri2 = fri.strftime('%Y-%m-%d')
	#fri2 = "2023-03-17"
	#e: [2023-04-21,
	stock = inp[0]
	#stock =str(input("stock = "))
	#go =str(input("get from yahoo finance, 1 for yes, blank for no = "))
	go = "1"
	tim2 = tim.strftime('%H=%M--%m.%d')
	stock = stock.upper()
	#fri2 = "2023-04-21"
	print (fri2,stock,go)
	#sta = sta+datetime.timedelta(7*(dif-1))
	print ("exp = ",fri2)
	#print (now3)
	#print (now,now2,now3,day)
	cwd = os.getcwd()
	fea =cwd+"\\ear"
	#fea =cwd 
	lis = os.listdir(fea)
	fic = fea+"\\"+stock+".0call."+tim2+'.csv'
	fip = fea+"\\"+stock+".0put."+tim2+'.csv'
	#pri(lis)
	print (fip,fic)
	get = 0

	if "1" in go:	
		if fip not in lis:
			if fic not in lis:
				import yfinance as yf
				cha = yf.Ticker(stock)
				#che = cha.options
				#che = cha.earnings
				#print (che)
				#sye()
				try:
					opt = cha.option_chain(fri2)
				except:
					print ("waiting to requery for new friday..")
					sle([5])
					#cha = yf.Ticker(stock)
					aga = "2023-04-21"
					opt = cha.option_chain(aga)
				put = opt.puts
				cal = opt.calls 
				#print (type(opt))
				#print(put,cal)
				put.to_csv(fip)
				cal.to_csv(fic)
				get = 1
			
	if get==0:
		print("already in file")
	calls = csr([fic])
	puts = csr([fip])

	matc = []
	matc.append("volume")
	matc.append("contractSymbol")
	matc.append("strike")
	matc.append("bid")
	matc.append("ask")
	
	matp = []
	matp.append("bid")
	matp.append("ask")
	matp.append("strike")
	matp.append("contractSymbol")
	matp.append("volume")

	for a,val in enumerate(matc):
		ind = calls[0].index(val)
		new = [val,ind]
		matc[a] = new

	for a,val in enumerate(matp):
		ind = puts[0].index(val)
		new = [val,ind]
		matp[a] = new
	pri(matc)
	pri(matp)
	mas = []
	for a,val in enumerate(calls):
		app = []
		for b, valb in enumerate(matc):
			app.append(val[valb[1]])
		mas.append(app)
	pri(mas)
	tem = []
	for a,val in enumerate(puts):
		app = []
		for b, valb in enumerate(matp):
			app.append(val[valb[1]])
		tem.append(app)
	pri(tem)
	for a,val in enumerate(mas):
		str1 = val[2]
		for b,valb in enumerate(tem):
			str2 = valb[2]
			if str1==str2:
				mas[a]=mas[a]+["--"]+valb
	pri(mas)
	vols = []
	ind = "none"
	for a,val in enumerate(mas):
		if a==0:
			continue
		vol = val[0]
		print("vol",vol)
		try:
			vol = float(val[0])
		except:
			continue
		vols.append(vol)
	print (vols)
	vmax = max(vols)
	imax = vols.index(vmax)
	print(vmax,imax)
	dif = 10

	sma=[]
	for a,val in enumerate(mas):
		try:
			rat = float(val[4])/float(val[7])
		except:
			continue
		rat = rat-1
		rat = abs(rat)
		new = [rat]
		new = new+val
		print (new)
		sma.append(new)
	lit = []
	for a,val in enumerate(sma):
		lit.append(val[0])
	litv = min(lit)
	liti = lit.index(litv)
	pri(lit)
	print(litv,liti)
	sma2 = []
	for a,val in enumerate(sma):
		new = val[1:len(val)]
		sma2.append(new)
	
	pri(sma2)
	#sye()

	mas2 = [mas[0]]
	dif2 = dif
	che = liti-dif
	if che<0:
		dif2 = liti
	mas2 = mas2+sma2[liti-dif2:liti]
	mas2 = mas2+[["---"]]
	mas2 = mas2+[sma2[liti]]
	mas2 = mas2+[["---"]]
	dif3 = dif
	che = liti+dif
	if che>len(sma2):
		dif3 = len(sma2)-liti
	mas2 = mas2+sma2[liti+1:liti+dif3]

	pri(mas2)
	#sye()
	sav = fea+"\\"+stock+".0opt."+tim2
	xlw([sav,"xlsx",mas2])
	if get==0:
		print("already in file")
	ope = sav+".xlsx"
	sw(ope,1)
	hod3(["win","left",1,0])

inp = []
der([str(input("stock = "))])