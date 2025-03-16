exec(open('util.py').read())
def adv(inp):
	
	sea =str(input("search term = "))
	url = []
	
	url1 = "https://shop.advanceautoparts.com/web/SearchResults?searchTerm="
	url2 = sea
	url3 = "&filterValue=unbxd_DeliveryMethod_uFilter%3AFree+In-Store+Pickup&sortBy=PRICE_LOW_HIGH&storeId=10151&catalogId=10051&langId=-1"
	har = url1+url2+url3
	url.append(har)	

	num4([url,2])	
	
	"""
	if len(url)==3:
		alt(1,1)
		opt2([url,0])

	if len(url)>3:
		num4([url,2])	
		"""	


inp = []
adv(inp)