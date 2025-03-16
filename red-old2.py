exec(open('util.py').read())
def red(inp):

	inp = whi("search for? = ")
	
	lis = []
	lis.append(["con","construction"])
	lis.append(["too","tools"])
	lis.append(["car","careeradvice"])
	lis.append(["car","careerguidance"])
	lis.append(["tra1","api"])
	lis.append(["tra2","trading212"])
	lis.append(["tra3","algotrading"])
	lis.append(["tra3","trading"])
	lis.append(["tra3","stocks"])
	lis.append(["csc","cscareerquestions"])

	url = []

	for a,val in enumerate(inp):
		for b,val2 in enumerate(lis):
			if val in val2[0]:
				inp[a] = val2[1]

	pri(inp)
	#sye()
	url = []
	for a,val in enumerate(inp):
		nex = "https://www.reddit.com/r/"+val+"/submit"
		url.append(nex)

	pri(url)
	#sye()

	num4([url,2])






inp = []
red(inp)