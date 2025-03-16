exec(open('util.py').read())
def ear6(inp):
	cwd = os.getcwd()
	fea =cwd+"\\ear" 
	lis = os.listdir(fea)
	che = "dat.csv"
	if che not in lis:		
		key = "FK98MBU38O64HAMH"
		url = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey='+key
	
		dat = requests.get(url)
		url_content = dat.content
	
		des = fea+"\\"+che
		#csv_file = open("dat.csv", 'wb')
		csv_file = open(des, 'wb')
	folder
		csv_file.write(url_content)
		csv_file.close()	
		naw = "naw"
	
	mas = []

	fil = fea+"\\"+"dat.csv"

					
	with open(fil, newline='') as csvfile:
	
	    reader = csv.reader(csvfile)
	    for row in reader:
	    	cur = row[5]
	    	if "USD" not in cur:
	    		continue
	    	mas.append(row)

	from datetime import date
	now = date.today() 
	now2 = now.strftime('%m/%d/%Y')
	now3 = datetime.datetime.strptime(now2,'%m/%d/%Y')
	now = now3

	day = now.weekday()
	"""
	0 = this week
	-1 = 1 week back
	2 = 2 weeks forward, etc..
	"""
	dif = 1

	sta = ""
	end = ""
	#sta = next monday
	mov = 7-day
	sta = now+datetime.timedelta(mov)
	sta = sta+datetime.timedelta(7*(dif-1))

	end = sta+datetime.timedelta(6)

	vie = []
	for a,val in enumerate(mas):
		pro2([a,len(mas),val])
		if a==0:
			continue
		sto = val[0]
		nam = val[1]
		rel = val[2]
		ide1 = "-"
		ide2 = "-"
		fin = rel.find(ide1)
		fin2 = rel.find(ide2,fin+1)
		year = rel[0:fin]
		if len(str(year))==1:
			year = "0"+year
		mon = rel[fin:fin2]
		if len(str(mon))==1:
			mon = "0"+mon
		mon = mon.replace(ide1,"")
		day = rel[fin2:len(rel)]
		day = day.replace(ide2,"")
		sep1 = "/"
		sep2 = "/"
		rel2 = mon+sep1+day+sep2+year
		dat = datetime.datetime.strptime(rel2,'%m'+sep1+'%d'+sep2+'%Y')
		if dat>=sta:
			if dat<=end:
			
				vie.append([sto,rel2,nam])
	
	che = "mas.xlsx"
	if che not in lis:
		ray = []
		hit = ["NYSE","NASDAQ","AMEX"]
		for a,val in enumerate(lis):
			for b,val2 in enumerate(hit):
				if val2 in val:
					fil = fea+"\\"+val
					rea2 = rec([fil])
					for c,val3 in enumerate(rea2):
						ray.append(val3)
					break

				
		#pri(ray)
		ray2 = []
		for a,val in enumerate(ray):
			sto = val[0]
			cos = val[5]
			vol = val[6]
			try:
				vtp = float(cos)*float(vol)
			except:
				continue
			vtp = vtp/1000000	
			vtp = int(vtp)
			app = [vtp,sto,cos,vol]
			ray2.append(app)
		ray2.sort(reverse=True)
	
		xlw(["mas","xlsx",ray2]) 


	fil = fea+"\\"+che		
	loa = xlr([fil,"xlsx"])

	wha =[]
	for a,val in enumerate(vie):
		sto1 = val[0]
	
		for b,val2 in enumerate(loa):
			sto2 = 	val2[1]
			if sto1==sto2:
				app = [val2[0],val2[1],val[1],val[2]]
				wha.append(app)
				break

	lis = os.listdir(fea)
	import yfinance as yf	
	
	exp1 = "pri"
	exp2 = "xls"
	exp = "."+exp1+"."+exp2
	"""
	exs1 = "spe"
	exs2 = "xls"
	exs = "."+exs1+"."+exs2

	exd1 = "dat"
	exd2 = "xls"
	exd = "."+exd1+"."+exd2
	"""


	exs = ".spe"
	
	exd = ".dat"
	exd1 = "dat"
	exd2 = "json"
	exd = "."+exd1+"."+exd2


	get = []
	for a,val in enumerate(wha):
		sto = val[1]
	
		che = sto+exp
		print(che)
		if che not in lis:
			get.append(sto)

	for a,val in enumerate(get):
	
		pro = yf.Ticker(val)
		#hist = pro.history(period="max")
		hist = pro.history(period="5y")
	
		#hist.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')
		fil = fea+"\\"+val
		hist = hist[::-1]
	
		fil = fil+exp
	
	
		#xls2([hist,fil])
		wri2([fil,hist])
		pro2([a+1,len(get),val])
		print(str(len(get)-a)+" remaining for yfinance..."+fil)
		sle([15])

	lis = os.listdir(fea)
	get = []

	ead = exd
	for a,val in enumerate(wha):
		sto = val[1]
		if sto+ead not in lis:
			get.append(sto)

	key = "FK98MBU38O64HAMH"
	ray = get
	for a,val in enumerate(ray):
		url = "https://www.alphavantage.co/query?function=EARNINGS&symbol="+val+ "&apikey="+key
		req = requests.get(url)
		data = req.json()
		sav = fea+"\\"+val+ead
	
		with open(sav, 'w') as f:
		    json.dump(data, f)
	
		#print (data)
		sou = "alpha vantage"
		pro3([sou,a,ray,val])
		sle([21])
		
	lis = os.listdir(fea)
	nam = sta.strftime("%Y-%m-%d")
	nam2 = sta.strftime("%m-%d")
	
	fil = "nawnaw"
	if fil not in lis:
		mot = []
		for a,val in enumerate(wha):
			sym = val[1]
			vtp = val[0]
		
			dat = val[2]
			nam = val[3]
			get = fea+"\\"+sym+ead
		
			try:
				eah = js2([get])
			except:
				continue
		
			try:
				eah2 = eah["quarterlyEarnings"]
			except:
				continue
			dats = []
			for b,val2 in enumerate(eah2):
				if b==10:
					break
				red = val2["reportedDate"]
			
				dats.append(red)
			fip = fea+"\\"+sym+exp
			print(fip )
			prh = rea([fip])
		
			prh.reverse()
		
			#pri(prh[0:100])
		
			#print ("")
		
			app = []
			cor = ""
			for b,val2 in enumerate(dats):
				mov = []
				for c,val3 in enumerate(prh):
					if val2 in val3[0]:
					
						mov.append(prh[c-1])
						mov.append(val3)
						mov.append(prh[c+1])
					
				aft = -5
			
				if len(mov)==0:
					continue
				che1 = mov[1][5]
				che2 = mov[2][5]
				che3 = str(che1)+str(che2)
				if "Vol" in che3:
					continue
				if float(mov[1][5])>float(mov[2][5]):
					aft = 1
				if float(mov[2][5])>float(mov[1][5]):
					aft = 2
				for c,val3 in enumerate(mov):
					for d in range(1,5):
						try:
							val3[d] = dec([val3[d],2])
						except:
							continue
					
					if c==aft:
						dayb = float(mov[c-1][4])
						ope = float(val3[1])
						hig = float(val3[2])
						low = float(val3[3])
						clo = float(val3[4])
						try:
							gap = mad([ope,dayb])
						except:
							continue
						up = mad([hig,ope])
						dow = mad([low,ope])
						fou = mad([clo,ope])
						add = [gap,up,dow,fou]

						if "-" in str(gap):
							if abs(dow)>abs(up):
								cor = cor+"c"
							if abs(up)>abs(dow):
								cor = cor+"r"

						if "-" not in str(gap):
							if abs(up)>abs(dow):
								cor = cor+"c"
							if abs(dow)>abs(up):
								cor = cor+"r"

					
						val3 = val3+add
					app.append(val3)
				app.append("")
			win = ["cccc","rrrr"]
		
			cor3 = ""
			if cor[0:4] in win:
				cor1 = cor[0:4]
				cor1 = cor1.upper()
				cor2 = cor[4:len(cor)]
				cor3 = cor1+cor2
			
			#if cor[0:4]==
			win2 = ["CCCC","RRRR"]
			val.append(cor3)
			val.append(cor)
			mot.append(val)
			sav = fea+"\\"+sym+exs
		
			wri2([sav,app])
		
			tex = "gen specific.."
			pro3([tex,a,wha,val])
	


		mot.sort()
		mot.sort(reverse=True)
		mot.sort(key=lambda x:x[4],reverse=True)
		pri(mot)
		


		hea = []
		hea.append("vol*pri")
		hea.append("sym")
		hea.append("date")
		hea.append("company")
		hea.append("cap")
		hea.append("his")
		hea = [hea]
		mot = hea+mot

		sav = nam2
		sav = fea+"\\"+nam2
	
	
		wri2([sav,mot])



inp = []
ear6(inp)