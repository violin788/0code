exec(open('util.py').read())
def der(inp):
	from datetime import date
	now = date.today() 
	now2 = now.strftime('%m/%d/%Y')
	now3 = datetime.datetime.strptime(now2,'%m/%d/%Y')

	#os.path.getctime('file_path')
	tim = datetime.datetime.now()
	tim2 = tim.strftime('%H-%M...%m.%d')
	#tim2 = datetime.datetime.strptime(tim,'%H:%M:%S')
	print (tim2)
	#sye()

	day = now.weekday()
	#day = 5
	cha = 0
	if day<4:
		cha = 4-day
	if day>4:
		cha = 7-(day-4)
	fri = now+datetime.timedelta(cha)
	fri2 = fri.strftime('%Y-%m-%d')
	fri2 = "2023-03-17"
	#sta = sta+datetime.timedelta(7*(dif-1))
	print ("exp = ",fri2)
	#print (now3)
	#print (now,now2,now3,day)
	cwd = os.getcwd()
	fea =cwd+"\\ear"
	#fea =cwd 
	lis = os.listdir(fea)
	#stock =str(input("stock = "))
	#hour =str(input("hour = "))
	#minute =str(input("minute = "))
	#stock = "spy"
	stock =str(input("stock = "))
	go =str(input("get from yahoo finance,1 for yes,0 for no = "))
	
	stock = stock.upper()

	#tim2
	#fic2 = stock+".0call."++'.csv'
	print (tim2)
	#sye()

	#14-14...03.14
	#tim2 = "14-06...03.14"
	fic = fea+"\\"+stock+".0call."+tim2+'.csv'
	fip = fea+"\\"+stock+".0put."+tim2+'.csv'
	pri(lis)
	print (fip,fic)
	get = 0

	if "1" in go:	
		if fip not in lis:
			if fic not in lis:
				import yfinance as yf
				cha = yf.Ticker(stock)
				opt = cha.option_chain(fri2)
				put = opt.puts
				cal = opt.calls 
				#print (type(opt))
				#print(put,cal)
				put.to_csv(fip)
				cal.to_csv(fic)
				get = 1
			
			
	if get==0:
		print("already in file")
	pud = csr([fip])
	cad = csr([fic])
	"""
	strike
	bid
	ask
	contractSymbol
	"""
	mat = []
	mat.append("contractSymbol")
	mat.append("bid")
	mat.append("ask")
	mat.append("strike")
	matp = []
	matp.append("strike")
	matp.append("bid")
	matp.append("ask")
	matp.append("contractSymbol")
	#ind = []
	mas = []
	hea = []
	hea.append("contractSymbol")
	hea.append("bid")
	hea.append("ask")
	hea.append("strike")
	hea.append("strike")
	hea.append("bid")
	hea.append("ask")
	hea.append("contractSymbol")
	mas.append(hea)
	vmax = "none"
	imax = "naw"
	for a,val in enumerate(cad):
		if a==0:
			mat2 = []
			for b,valb in enumerate(mat):
				ind = val.index(valb)
				mat2.append([valb,ind])
				#mat2.append(val.index([valb]))
			voli = val.index("volume")
			#voli = val.index("percentChange")
			#percentChange

			#percentChange as opposed to volume..gives correct

			vols = []
			print (voli)
			#sye()
			for b,valb in enumerate(cad):
				#print (valb[voli])
				vol = valb[voli]
				if "volume" in vol:
					continue
				if vol=="":
					continue
				vol = vol.replace(".0","")
				vol = int(vol)
				vols.append(vol)
			#vols.sort(reverse=True)
			#print (vols)
			vmax = max(vols)
			print(vmax)
			imax = vols.index(max(vols))
			print (vmax,imax)
			#sye()
	sid = 10
	inc = 0
	for a in range(imax-sid,imax+sid):
		inc = inc+1
		if inc==sid:
			mas.append("")
		if inc==sid+1:
			mas.append("")
		val = cad[a]
		app = []
		for b,valb in enumerate(mat2):
			app.append(val[valb[1]])
		mas.append(app)
	pri(mas)
	sam =[]
	for a,val in enumerate(pud):
		if a==0:
			mat2 = []
			for b,valb in enumerate(matp):
				ind = val.index(valb)
				mat2.append([valb,ind])
				#mat2.append(val.index([valb]))
		if a>0:
			app = []
			for b,valb in enumerate(mat2):
				app.append(val[valb[1]])
			sam.append(app)
			#mas.append(app)
	for a,val in enumerate(sam):
		st1 = val[0]
		for b,valb in enumerate(mas):
			try:
				st2 = valb[3]
			except:
				continue
			if st1==st2:
				mas[b] = mas[b]+val
	pri(mas)
	#META.0put.12-11.PM.03-14-2023
	

	sav = fea+"\\"+stock+".0opt."+tim2
	xlw([sav,"xlsx",mas]) 
	sye()

	#03-14-2023.10:54.AM

	for a,val in enumerate(mat):
		#0 = match, 1 = put index, 2  = call index
		ind1 = cad[0].index(val)
		ind2 = pud[0].index(val)
		mat[a] = [val,ind1,ind2]
		print ("mat[a]",mat[a])
	pri(mat)
	sye()
	pri(pud)
	#print (pud)
	#print (cad)
	if get==0:
		print("already in file")

inp = []
der(inp)