exec(open('util.py').read())
def tax(inp):
	def tax3(inp):
		#bac = tax3([yes,fed])
		yes = inp[0]
		rat = inp[1]
		bac = []
		for a,val in enumerate(rat):
			#spe = val
			cen = val[0]
			cen2 = cen/100
			low = val[1]
			hig = val[2]
			pay = ""
			tao = ""
			if yes<low:
				break
			if yes>=low:
				if "inf" in str(hig):
					tao = yes-low
				if "inf" not in str(hig):
					if yes<hig:
						tao = (yes-low)
					if yes>=hig:
						tao = (hig-low)
			pay = cen2*tao
			pay2 = dec([pay,2])
			spe = [pay2,tao]+val
			spe[2] = str(spe[2])+"%"
			bac.append(spe)
		return bac
	
	#emi = 174000
	emi = 10000000
	sei = 0
	ded=12000
	inc = emi+sei
	#emt = employment type, se for self employed, em for employed
	emt = "em"
	yes=inc-ded
	if yes<0:
		yes=0
	fed = []
	#fed.append([percentage rate,min of bracket,max of bracket])
	fed.append([10,0,9950])
	fed.append([12,9950,40525])
	fed.append([22,40525,86375])
	fed.append([24,86375,164925])
	fed.append([32,164925,209425])
	fed.append([35,209425,523600])
	fed.append([37,523600,"inf"])
	#inp = [fed,yes]
	sta=[]
	sta.append([2,0,3000])
	sta.append([3,3000,5000])
	sta.append([5,5000,17000])
	sta.append([5.75,17000,"inf"])
	tot = []
	tot.append(["Employed Income",emi])
	tot.append(["Self Employed Income",sei])
	tot.append(["Gross Income",inc])
	tot.append(["Standard Deduction",ded])
	tot.append(["Taxable Income",yes])
	hea = [["From Bracket", "Taxable in Bracket,","%","Min Bracket","Max Bracket"]]
	tot.append(hea)
	fet = 0
	fed2 = tax3([yes,fed])
	tot = tot+fed2
	stt = 0
	#tot.append(["State Income Taxes = ",stt])
	tot.append(hea)
	sta2 = tax3([yes,sta])
	tot = tot+sta2
	for a,val in enumerate(fed2):
		fet = fet+int(val[0])
	for a,val in enumerate(sta2):
		#print(val)
		stt = stt+int(val[0])
	for a,val in enumerate(tot):
		sea = val[0]
		if "Federal Income Taxes" in str(sea):
			tot[a][1]=fet
		if "State Income Taxes"  in str(sea):
			tot[a][1]=stt
	ttp = fet+stt
	med1 = 1.45
	soc1 = 6.2
	med2 = 2.9
	soc2 = 12.4
	tog = []
	soce = (soc1/100)*emi
	mede = (med1/100)*emi
	socs = (soc2/100)*sei
	meds = (med2/100)*sei
	fict = soce+mede+socs+meds
	muc = dec([(((ttp+fict)/inc)*100),2])
	muc2 = str(muc)+"%"
	aft = inc-ttp-fict
	aft52 = dec([aft/52,2])
	aft4 = dec([aft52*4,2])
	mon = dec([aft/12,2])

	tog.append(["Federal Income Taxes = ",fet])
	tog.append(["State Income Taxes = ",stt])
	tog.append(["FICA total",fict])
	ttp2 = fet+stt+fict
	tog.append(["Fed income tax+state income tax+FICA",ttp2])
	#tog.append(["Income Tax to Pay",ttp2])
	#tog.append(["Fed income tax+state income tax+FICA =",(ttp+fict+)])
	tog.append(["%"+" of income in taxes =",muc2])
	tog.append(["Salary per week.. = ",aft52])
	tog.append(["Salary per 4 weeks.. = ",aft4])
	tog.append(["Salary per month.. = ",mon])
	tog.append(["Employed - Social Security",soce])
	tog.append(["Employed - Medicare",mede])
	tog.append(["Self Employed - Social Security",socs])
	tog.append(["Self Employed - Medicare",meds])
	ind = ""
	for a,val in enumerate(tot):
		che = val[0]
		if "Taxable Income" in che:
			ind = a
			break
	tot2 = tot[0:ind+1]+tog+tot[ind:len(tot)]
	tot = tot2
	pri(tot)
inp = []
tax(inp)