exec(open('util.py').read())
def beg(inp):
	inp = inp
	fol = os.getcwd()
	fol = fol+"\\ren"
	print (fol)
	lis = os.listdir(fol)
	print (lis)
	rep = []
	rep.append([".mp3","aud-"])
	rep.append([".apk","apk-"])
	rep.append([".jpg","img-"])
	rep.append([".png","img-"])
	rep.append([".gif","img-"])
	rep.append([".mp4","mov-"])
	rep.append([".pdf","pdf-"])
	for a,val in enumerate(lis):
		ski = 0	
		for b,val2 in enumerate(rep):
			che = val2[0]
			if che in val:
				che2 = val2[1]
				if che2 in val:
					break
				if che2 not in val:
					new = che2+val
					new = fol+"\\"+new
					old = fol+"\\"+val
					print (a,new)
					print (old)

					os.rename(old,new)
inp = []
beg(inp)