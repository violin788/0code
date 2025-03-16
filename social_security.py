exec(open('util.py').read())
def soc(inp):
	
	loa1 = rea(["soc.xls"])
	#pri(loa1)

	loa2 = []
	for a,val in enumerate(loa1):
		try:
			fir = float(val[0])
		except:
			continue
		loa2.append(val)
	pri(loa2)
	tot = 0
	for a,val in enumerate(loa2):
		yea = val[1]
		#print (val[1])
		if len(str(yea))>0:
			yea = float(yea)
			tot = tot+yea
	print(tot)
	mon = tot/420
	print(mon)
	"""
	tot = 0
	for a,val in enumerate(loa2):
		print(yea)
		yea = val[1]
		tot = tot+float(yea)
	print(tot)
	"""

	"""
	(a) 90 percent of the first $1,115 of his/her average indexed monthly earnings, plus 
    (b) 32 percent of his/her average indexed monthly earnings over $1,115 and through $6,721, plus 
    (c) 15 percent of his/her average indexed monthly earnings over $6,721.
	"""


inp = []
soc(inp)