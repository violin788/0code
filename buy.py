exec(open('util.py').read())
def buy(inp):
	inputs = whi("search for? = ")
	replacement_value = "_____"
	url_amazon = "https://www.amazon.com/s?k="+replacement_value+"&s=price-asc-rank&qid=1668288142&ref=sr_st_price-asc-rank&ds=v1%3AMtPpiCm9u5Ea%2B0Uh0kHzGAxiJCgkhbR4KIvEqo352OY"
	url_ebay = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="+replacement_value+"&_sacat=0&LH_PrefLoc=3&_sop=15&rt=nc&LH_BIN=1&_ipg=240"
	urls = [url_amazon,url_ebay]
	urls2 = []
	for a,val in enumerate(inputs):
		for b,valb in enumerate(urls):
			new_url = valb.replace(replacement_value,val)
			urls2.append(new_url)
	urls = urls2
	pri(urls)

	pause = 0
	for a,val in enumerate(urls):
		pause = pause+1
		url = val
		command = "start \"\" "+url
		os.system(command)
		time.sleep(1)
		#single_url([url,2])	
		if pause==2:
			wait = 3
			time.sleep(wait)
			print("waiting "+str(wait)+" seconds..")
			pause = 0

		"""
	ler = 2
	sye()
	command = "python -m py_compile "+out_file
	os.system(command)
	if len(url)==ler:
		alt(1,1)
		opt2([url,0])

	if len(url)>ler:
		num4([url,2])	
	#num4([url,2])
	"""
inp = []
buy(inp)