exec(open('util.py').read())
def mp3(inp):
	inp = inp
	fol = os.getcwd()+"\\mp3"
	lis = os.listdir(fol)
	for a,val in enumerate(lis):
		if ".mp4" in val:
			rep = val.replace(".mp4",".mp3")
			if rep not in lis:
				print (a,val)
				beg = fol+"\\"+val
				end = fol+"\\"+rep
				clip = (VideoFileClip(beg))
				#clip.write_gif(end,fps=15)
				clip.audio.write_audiofile(end)
inp = []
mp3(inp)