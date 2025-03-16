exec(open('util.py').read())
def ord(inp):
	inp =str(input("search = "))
	url = []
	url.append("https://www.ebay.com/sch/i.html?_from=R40&_nkw="+inp+"&_sacat=0&_sop=15")
	url.append("https://www.amazon.com/s?k="+inp+"&s=price-asc-rank&crid=58QYKCV6PA6U&qid=1652278970&sprefix=mobile+solderi%2Caps%2C1072&ref=sr_st_price-asc-rank")
	pri(url)
	sye()

	num4([url,1])
inp = []
ord(inp)