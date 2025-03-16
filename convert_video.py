exec(open('util.py').read())
def tru(ray):
	ray = ray
	import cv2
	#file_path = "./video.avi"  # change to your own video path
	fil = "fly.mp4"
	out = "fly2.mp4"
	vid = cv2.VideoCapture(fil)
	hei = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
	wid = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
	fps = vid.get(cv2.CAP_PROP_FPS)
	print (hei,wid,fps)
	res = 6

	hei = hei/res
	wid = wid/res

	print (hei,wid)

	import moviepy.editor as mp
	clip = mp.VideoFileClip(fil)
	new = clip.resize( (wid,hei) )
	new.write_videofile(out)
	

from moviepy.editor import *inp = []
tru(inp)