exec(open('util.py').read())
def loc(inp):

	inp = whi("search for? = ")
	tem = "_____"
	ama = "https://www.amazon.com/s?k="+tem+"&s=price-asc-rank&qid=1668288142&ref=sr_st_price-asc-rank&ds=v1%3AMtPpiCm9u5Ea%2B0Uh0kHzGAxiJCgkhbR4KIvEqo352OY"
	eba = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+tem+"&_sacat=0&LH_PrefLoc=3&_sop=15&rt=nc&LH_BIN=1&_ipg=240"
	bas = [ama,eba]


	#"https://www.ebay.com/sch/i.html?_from=R40&_nkw="
	#dewalt+charger


	url = []
	for a,val in enumerate(inp):
		sea = val
		for b,val2 in enumerate(bas):
			app = val2.replace(tem,sea)
			url.append(app)
			
	pri(url)

	ler = 2
	if len(url)==ler:
		alt(1,1)
		opt2([url,0])

	if len(url)>ler:
		num4([url,2])	

	#num4([url,2])



inp = []
loc(inp)