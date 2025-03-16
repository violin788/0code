exec(open('util.py').read())
def loc(inp):

	inp = whi("search for? = ")

	tem = "_____"
		
	cra = "https://fredericksburg.craigslist.org/search/sss?sort=priceasc&query="+tem
	fac ="https://www.facebook.com/marketplace/103795126325698/search/?deliveryMethod=local_pick_up&sortBy=price_ascend&query="+tem+"&exact=false"	
	zic = "22401"
	eba = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+tem+"&_sacat=0&_stpos="+zic+"&_sadis=25&LH_PrefLoc=99&_fspt=1&_sop=15"
	bas = [cra,fac,eba]

	url = []
	for a,val in enumerate(inp):
		sea = val
		for b,val2 in enumerate(bas):
			app = val2.replace(tem,sea)
			url.append(app)
			
	pri(url)

	if len(url)==3:
		alt(1,1)
		opt2([url,0])

	if len(url)>3:
		num4([url,2])		





inp = []
loc(inp)