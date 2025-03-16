exec(open('util.py').read())
def vid(inp):
	"""
	320 × 240   240p
	640 x 360   360p
	640 x 480	480p
	1280 x 720	720p
	1920 x 1080 1080p
	"""	
	inp = inp
	fol = os.getcwd()+"\\mov"
	lis = os.listdir(fol)
	print(fol,lis)
	lis2 = []
	ray = []
	for a,val in enumerate(lis):
		#if ".new" in val:
		#	continue
		loc = fol+"\\"+val
		siz = os.path.getsize(loc)
		print (loc,siz)
		new = [siz,loc]
		#new.append([siz,loc])
		lis2.append(new)
	lis2.sort()
	dis(lis2)
	for a,val in enumerate(lis2):
		#if ".new" in val:
		#	continue
		print("val",val)
		#loc = fol+"\\"+val[1]
		loc = val[1]
		siz = os.path.getsize(loc)
		print (loc,siz)
		#continue 
		clip = VideoFileClip(loc)

		w1 = clip.w
		h1 = clip.h		 
		print("Width x Height of clip 1 : ", end = " ")
		print(str(w1) + " x ", str(h1))

		"""
		320 × 240   240p
		640 x 360   360p
		640 x 480	480p
		1280 x 720	720p
		1920 x 1080 1080p
		"""	
	
		tab = []
		tab.append([320,240])
		tab.append([640,360])
		tab.append([640,480])
		tab.append([1280,720])
		tab.append([1920,1080])
		#tab.append([320,240])

		wid = 1280
		hei = 720
		#inputs
		if ".new" in val:
			continue
		rat = 1
		beg = 0
		end = 68

		if rat!=1:
			wid = w1*rat
			hei = h1*rat
			clip = clip.resize(newsize=(hei,wid))
		#clip2 = clip1.resize(rat)
		if end!=0:
			clip = clip.subclip(beg,end)

		w2 = clip.w
		h2 = clip.h
		print("Width x Height of clip 2 : ", end = " ")
		print(str(w2) + " x ", str(h2))
		
		new = loc.replace(".mp4",".new."+str(int(wid))+"x"+str(int(hei))+".mp4")
		clip.write_videofile(new)
	inp = []
vid(inp)