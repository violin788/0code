exec(open('util.py').read())
def use(inp):
	#inp = inp
	#sea =str(input("item = "))
	sea = whi3(["depart = "])
	print (sea)
	#ssye()
	#url2 = []
	url1 = []
	for a,val in enumerate(sea):
		eba = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+val+"&_sacat=0&LH_TitleDesc=0&LH_PrefLoc=99&_stpos=22401&_sadis=25&_fspt=1&_sop=15&rt=nc"
		cra = "https://fredericksburg.craigslist.org/search/sss?query="+val+"&sort=priceasc#search=1~gallery~0~0"
		fac = "https://www.facebook.com/marketplace/103795126325698/search?deliveryMethod=local_pick_up&sortBy=price_ascend&query="+val+"&exact=false"
		url2 = []
		url2.append(eba)
		url2.append(cra)
		url2.append(fac)
		opa3(["loc",url2])
		#opa3(["loc"])

		#url1.append(url2)
	#opt4([url1])
	#opt3([url1])

	"""
	for a,val in enumerate(url1):
		opt2([val,0])
	pri(url)




	opt2([url,0])

	nu(url,1)
	sye()

	for a,val in enumerate(url2):
		opt2([val,0])
	sye()
	opt2([urr,0])
	"""
inp = []
use(inp)