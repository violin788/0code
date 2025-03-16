exec(open('util.py').read())
def sho3(ray):

	url_array = []
	search_for =str(input("search for = "))
	url_array.append("https://www.ebay.com/sch/i.html?_from=R40&_nkw="+search_for+"&_ipg=200&LH_BIN=1&_sop=15&_oac=1&rt=nc&LH_PrefLoc=3")
	url_array.append("https://www.amazon.com/s?k="+search_for+"&s=price-asc-rank&qid=1622905018&ref=sr_st_price-asc-rank")
	url_array.append("https://www.google.com/search?q="+search_for+"&rlz=1CAMURN_enUS956&sxsrf=ALeKk02dSOph7WXMS6zsLoJmD1SIattaaw:1622904706472&source=lnms&tbm=shop&sa=X&ved=2ahUKEwik26GU34DxAhV5FlkFHTmYAGcQ_AUoAXoECAEQAw")

	#nu(ray,1)
	file = "html_shop.html"
	gen_html([url_array,file])
	start_file([file,0])

inp = []
sho3(inp)