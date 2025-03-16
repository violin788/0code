exec(open('util.py').read())
def vid2(inp):
	inp = inp
	fol = os.getcwd()+"\\mov"
	lis = os.listdir(fol)
	for a,val in enumerate(lis):
		if ".mp4" in val:
			rep = val.replace(".mp4",".gif")
			if rep not in lis:
				print (a,val)
				beg = fol+"\\"+val
				end = fol+"\\"+rep
				clip = (VideoFileClip(beg))
				clip.write_gif(end,fps=15)
inp = []
vid2(inp)