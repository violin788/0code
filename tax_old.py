exec(open('util.py').read())
def tax(inp):
	#variables
	income=400000
	deduc=12000
	#emt = employment type, se for self employed, em for employed
	emt = "em"
	taxable=income-deduc
	
	fed=[]
	fed.append([10,[0,9950]])
	fed.append([12,[9950,40525]])
	fed.append([22,[40525,86375]])
	fed.append([24,[86375,164925]])
	fed.append([32,[164925,209425]])
	fed.append([35,[209425,523600]])
	fed.append([37,[523600,"inf"]])
	inp = [fed,taxable]

	var = ret_tax(inp)

	def tax2(inp):
		rat = inp[0]
		yes = inp[1]
		ret = []
		for a,val in enumerate(ray):


	fedi = var[0]
	brc = var[1]
	print("fed",var[0])
	dis(var[1])
	#sye()		

	sta=[]
	sta.append([2,[0,3000]])
	sta.append([3,[3000,5000]])
	sta.append([5,[5000,17000]])
	sta.append([5.75,[17000,"inf"]])
	inp2 = [sta,taxable]

	var2 = ret_tax(inp2)
	stai = var2[0]
	brc2 = var2[1]
	print("fed",var[0])
	dis(var2[1])
	print("stai",stai)
	#sye()		

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
	inf.append(["taxable income"+equ, taxable])
	inf.append(["employment status"+equ, emt])
	inf.append(["medicare rate"+equ, str(medicare_tax)])
	inf.append(["social security rate"+equ, str(social_secuity_tax)])
	inf.append(["medicare tax"+equ,med_tax,str(income)+"*"+str(medicare_tax)+"="+str(med_tax)])
	inf.append(["social security tax"+equ,soc_sec,str(income)+"*"+str(social_secuity_tax)+"="+str(soc_sec)])
	inf.append(["fica"+equ,fica,str(med_tax)+"+"+str(soc_sec)+"="+str(fica)])
	print ("tax",taxable)
	#sye()
	fer = []
	fei=0
	to_fed = fedi+fica
	tot = to_fed+stai
	taxp = tot/income
	taxp = to_percent(taxp)
	tah = income - tot
	tahm = int(tah/12)
	
	inf.append(["federal income tax"+equ, fedi])
	inf.append(["tax to federal government"+equ,to_fed,str(fica)+"+"+str(fedi)])
	inf.append(["state income tax"+equ, stai])
	inf.append(["federal+state tax"+equ, tot,str(to_fed)+"+"+str(stai)])
	inf.append(["percent tax"+equ,taxp])
	inf.append(["take home pay"+equ,tah])
	inf.append(["take home / month"+equ,tahm])
	
	#print ("federal income tax")
	#dis(fer)
	#print ("info")
	print ()
	dis(inf)
inp = []
tax(inp)