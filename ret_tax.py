exec(open('util.py').read())
def ret_tax(inp):
	fed = inp[0]
	taxable = inp[1]
	brc = []
	tgo = 0
	for a,val in enumerate(fed):
		bot = int(fed[a][1][0])
		top = fed[a][1][1]
		rat = (fed[a][0]/100)
		app = []
		spe = 0
		if bot>taxable:
			continue
		if type(top) is int:
			top = top
			if taxable>=top:
				dif = top-bot
				spe = dif*rat
				tgo = tgo+spe
				app = [spe,str(dif)+"*"+str(rat)+"="+str(spe),str(bot)+"-"+str(top)]
			if taxable<top:
				if taxable>=bot:
					dif = taxable-bot
					spe = dif*rat
					tgo = tgo+spe
					app = [spe,str(dif)+"*"+str(rat)+"="+str(spe),str(bot)+"-"+str(taxable)]
		if type(top) is str:
			top = taxable
			dif = taxable-bot
			spe = dif*rat
			tgo = tgo+spe
			app = [spe,str(dif)+"*"+str(rat)+"="+str(spe),str(bot)+"-"+str(top)]
		print(app)
		brc.append(app)
	ret = []
	ret.append(tgo)
	ret.append(brc)
	return ret
inp = []
ret_tax(inp)