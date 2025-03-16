exec(open('util.py').read())
def tax4(inp):

	#variables
	income=50000
	deduc=12000
	#emt = employment type, se for self employed, em for employed
	emt = "se"
	medicare_tax = 0
	social_secuity_tax = 0
	
	fed=[]
	fed.append([10,[0,9950]])
	fed.append([12,[9950,40525]])
	fed.append([22,[40525,86375]])
	fed.append([24,[86375,164925]])
	fed.append([32,[164925,209425]])
	fed.append([35,[209425,523600]])
	fed.append([37,[523600,"inf"]])
	#income=inp =str(input("input = "))
	inf = []
	if emt=="se":
		medicare_tax = .029
		social_secuity_tax = .124
	if emt=="em":
		medicare_tax = .0145
		social_secuity_tax = .062
	med_tax = income*medicare_tax
	soc_sec = income*social_secuity_tax
	fica = med_tax+soc_sec	
	equ = " = "
	inf.append(["gross income"+equ, income])
	inf.append(["standard dedudction"+equ, deduc])
	inf.append(["medicare tax"+equ, med_tax])
	inf.append(["social security tax"+equ, soc_sec])
	inf.append(["fica"+equ, fica])
	taxable=income-deduc
	fer = []
	fei=0
	fed_inc_tax = 0
	for a in range(0,len(fed)):
		app = 0
		bot = int(fed[a][1][0])
		top = fed[a][1][1]	
		rat = (fed[a][0]/100)
		try:
			top=int(top)
		except:
			if taxable>=bot:
				tao=taxable-bot
				app = rat*tao 
				fer.append([rat,app,str(taxable)+"-"+str(bot),tao,str(rat)+"*"+str(tao)])								
				fed_inc_tax = fed_inc_tax+app
				continue
		if taxable>=top:
			tao=top-bot
			app = rat*tao 
			fer.append([rat,app,str(top)+"-"+str(bot),tao,str(rat)+"*"+str(tao)])
		if taxable<top:
			if taxable>=bot:
				tao=taxable-bot
				app = rat*tao 
				fer.append([rat,app,str(taxable)+"-"+str(bot),tao,str(rat)+"*"+str(tao)])
		fed_inc_tax = fed_inc_tax+app	
	inf.append(["taxable income"+equ, taxable])
	inf.append(["federal income tax"+equ, fed_inc_tax])
	inf.append(["tax to federal government"+equ, fed_inc_tax+fica])
	print ("federal income tax")
	dis(fer)
	print ("info")
	dis(inf)		
inp = []
tax4(inp)