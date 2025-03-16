exec(open('util.py').read())
def pur(inp):

	inp = whi("search for? = ")
	replace_val = "-----search term-----"
	url = []
	url_ebay = []
	url_ebay.append("https://www.ebay.com/sch/i.html?_from=R40&_nkw=")
	url_ebay.append(replace_val)
	url_ebay.append("&_sacat=0&LH_BIN=1&LH_ItemCondition=3&LH_PrefLoc=3&_sop=15&_blrs=recall_filtering")
	url.append(url_ebay)
	amazon_url = []
	amazon_url.append("https://www.amazon.com/s?k=")
	amazon_url.append(replace_val)
	amazon_url.append("&i=electronics&rh=n%3A172282%2Cp_76%3A1249137011&s=price-asc-rank&dc&ds=v1%3AdVYCS7oUcX2RAaqLQWbjCez%2FUTfJDqlDkpOAuVtr8vs&crid=190LCKPA68FZ5&qid=1704816826&rnid=1249135011&sprefix=18.5v+3.5a%2Caps%2C125&ref=sr_st_price-asc-rank")
	url.append(amazon_url)
	walmart_url = []
	walmart_url.append("https://www.walmart.com/search?q=")
	walmart_url.append(replace_val)
	walmart_url.append("&sort=price_low")
	url.append(walmart_url)

	for a,val in enumerate(inp):
		if a==0:
			url2 = []
		for b,valb in enumerate(url):
			concat = ""
			for c,valc in enumerate(valb):
				if replace_val in valc:
					valb[c] = val
				concat = concat+valb[c]
			url2.append(concat)
	pri(url2)
	alt(1,1)
	opt2([url2,0])
	sye()

		#for b,valb in enumerate(val):


	pri(url)
	sye()




	url = []
	for a,val in enumerate(inp):
		sea = val
		for b,val2 in enumerate(bas):
			app = val2.replace(tem,sea)
			url.append(app)



	for a,val in enumerate(url2):
		opt2([val,0])

	
inp = []
pur(inp)