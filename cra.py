exec(open('util.py').read())
def cra(inp):
	inp = inp
	sea =str(input("search = "))
	price =str(input("price, in thouands = "))
	mile =str(input("mile, in thousands = "))
	suv =str(input("suv,1 for yes, blank for no = "))
	if suv=="1":
		suv = "&auto_bodytype=10"
	try:
		price = str(int(price)*1000)
	except:
		price = price
	try:
		mile = str(int(mile)*1000)
	except:
		mile = mile

	cit = []
	cit.append("charlottesville")
	cit.append("danville")
	cit.append("easternshore")
	cit.append("fredericksburg")
	cit.append("harrisonburg")
	cit.append("lynchburg")
	cit.append("blacksburg")
	cit.append("norfolk")
	cit.append("richmond")
	cit.append("roanoke")
	cit.append("swva")
	cit.append("winchester")
	cit.append("washingtondc")

	url = []
	if price!="":
		price = "&max_price="+price
	if mile!="":
		mile = "&max_auto_miles="+mile
	low = "1"
	if low!="":
		low = "&min_price="+low

	#&max_price=5000,&max_auto_miles=100000,&min_price=1
	sor = "&sort=priceasc"
	add = []
	add.append("fredericksburg")
	#add.append("richmond")
	add.append("washingtondc")
	ope = []

	for a,val in enumerate(cit):
		new = "https://"+val+".craigslist.org/search/sss?query="+sea+sor+price+mile+low+suv
		url.append(new)
		#if "washington" in val:
		#	rep = new.replace("craigslist.org","craigslist.org/nva")
		if val in add:
			ope.append(new)
			#if "washington" in val:
			#	ope.append(rep)
		#if "fredericksburg" in new:
		#	ope.append(new)
	dis(url)
	num4([ope,1])
	sye()
	"""
	#https://fredericksburg.craigslist.org/search/sss?query=xc60
    url.append("https://charlottesville.craigslist.org")
    url.append("https://danville.craigslist.org")
    url.append("https://easternshore.craigslist.org")
    url.append("https://fredericksburg.craigslist.org")
    url.append("https://harrisonburg.craigslist.org")
    url.append("https://lynchburg.craigslist.org")
    url.append("https://blacksburg.craigslist.org")
    url.append("https://norfolk.craigslist.org")
    url.append("https://richmond.craigslist.org")
    url.append("https://roanoke.craigslist.org")
    url.append("https://swva.craigslist.org")
    url.append("https://winchester.craigslist.org")
    url.append("https://washingtondc.craigslist.org")
    url.append("https://washingtondc.craigslist.org/nva")
    """
inp = []
cra(inp)