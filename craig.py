exec(open('util.py').read())
def craig(inp):

	search = whi("search for? = ")
	alt(1,1)
	for a,val in enumerate(search):
		print(a)
		#if a==0:
			
		url1 = "https://fredericksburg.craigslist.org/search/sss?query="
		search2 = val
		url2 = "&sort=priceasc#search=1~gallery~0~0"
		url = url1+search2+url2
			#if len(url)>3:
		single_url([url,0])
		#num5([url,2])	

	#url = url1+sea+url2
	
	#url1 = "https://fredericksburg.craigslist.org/search/sss?query="
	#bicycle
	#"&sort=priceasc#search=1~gallery~0~0"

inp = []
craig(inp)