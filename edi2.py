exec(open('util.py').read())
def edi2(inp):

	tex = rea4(["edi2","txt"])
	pri(tex)
	lin = nex([tex,"\n",0])
	pri(lin)
	ray = []
	for a,val in enumerate(lin):
		if len(val)==0:
			continue
		if "MB" in val:
			continue
		if "kB" in val:
			continue
		if ".mp3" in val:
			continue
		if "DOWNLOADED ALL" in val:
			continue
		val = val.replace(" D","")
		ray.append(val)
	pri(ray)
		

inp = []
edi2(inp)