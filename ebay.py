exec(open('util.py').read())
def ebay(inp):

	search = whi("search for? = ")

	for a,val in enumerate(search):
		print(a)
		if a==0:
			alt(1,1)
		url1 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
		search2 = val
		url2 = "&_sacat=0&_sadis=25&_stpos=22401&_fspt=1&_sop=15"
		#https://www.ebay.com/sch/i.html?_from=R40&_nkw=bicycle&_sacat=0&_sadis=25&_stpos=22401&_fspt=1&_sop=15
		url = url1+search2+url2
			#if len(url)>3:
		num5([url,2])	
	
inp = []
ebay(inp)