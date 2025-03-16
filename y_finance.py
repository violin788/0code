exec(open('util.py').read())
def yfi(inp):
	import yfinance as yf
	cwd = os.getcwd()
	fol = "ear"
	dire = cwd+"\\"+fol
	#sym = "CVS"
	sym =str(input("stock = "))
	sym = sym.upper()
	inf = yf.Ticker(sym).option_chain('2023-07-28')
	cal = inf.calls
	put = inf.puts
	#print(cal)
	#print(put)
	#print(type(cal),type(put))
	cal1 = sym+".cal.csv"
	put1 = sym+".put.csv"
	sav1 = dire+"\\"+cal1
	sav2 = dire+"\\"+put1
	cal.to_csv(sav1)
	put.to_csv(sav2)
	cal = rea([sav1])
	put = rea([sav2])
	cal2 = []
	for a,val in enumerate(cal):
		new = []
		"""
		new.append(float(val[3]))
		new.append(float(val[5]))
		new.append(float(val[6]))
		"""
		new.append(val[3])
		new.append(val[5])
		new.append(val[6])
		cal2.append(new)
	put2 = []
	for a,val in enumerate(put):
		new = []
		"""
		new.append(float(val[3]))
		new.append(float(val[5]))
		new.append(float(val[6]))
		"""
		new.append(val[3])
		new.append(val[5])
		new.append(val[6])
		put2.append(new)
	res = []
	for a,val in enumerate(cal2):
		new = []
		new.append(val[1])
		new.append(val[2])
		new.append(val[0])
		for b,valb in enumerate(put2):
			if new[2]==valb[0]:
				#new2 = []
				#try:
				new.append(valb[1])
				new.append(valb[2])
				new.append("")
				try:
					div1 = (float(new[0])+float(new[1]))/2
					div1 = dec([div1,2])
				except:
					continue
				div2 = (float(new[3])+float(new[4]))/2
				div2 = dec([div2,2])
				new.append(div1)
				new.append(div2)
				dif = abs(div1-div2)
				dif = dec([dif,2])
				new2 = []
				new2.append(dif)
				new2.append("")
				for c,valc in enumerate(new):
					new2.append(valc)
				res.append(new2)
				#res.append(new)
	pri(res)
	lis = []
	for a,val in enumerate(res):
		#lis.append(val[9])
		lis.append(val[0])
	pri(lis)
	low = min(lis)
	ind = lis.index(low)
	print(ind)
	res2 = res[ind-5:ind+5]
	pri(res2)

inp = []
yfi(inp)