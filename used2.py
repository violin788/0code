exec(open('util.py').read())
def use2(inp):
	inp = whi("search for? = ")
	probook = "https://www.ebay.com/sch/177/i.html?_dcat=177&_fsrp=1&_from=R40&_nkw=probook&LH_BIN=1&LH_ItemCondition=1000%7C1500%7C2000%7C2010%7C2020%7C2030%7C3000&_sop=15&_blrs=recall_filtering&rt=nc&LH_PrefLoc=3"
	hp_6560b = "https://www.ebay.com/sch/177/i.html?_dcat=177&_fsrp=1&_from=R40&_nkw=6560b&LH_BIN=1&LH_ItemCondition=1000%7C1500%7C2000%7C2010%7C2020%7C2030%7C3000&_sop=15&_blrs=recall_filtering&rt=nc&LH_PrefLoc=3"
	for a,val in enumerate(inp):
		if "probook" in val:
			inp[a] = probook
		if "6560b" in val:
			inp[a] = hp_6560b
	pri(inp)
	url = inp
	num4([url,2])
	#don't use other because do not do multiple open urls at ebay same millisecond?
	#alt(1,1)
	#opt2([url,0])

inp = []
use2(inp)