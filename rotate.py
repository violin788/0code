exec(open('util.py').read())
from moviepy.editor import *
	
def rot(inp):
	# Import everything needed to edit video clips
	#from moviepy.editor import *
	  
	# loading video dsa gfg intro video
	fil = "pol"
	typ = "mp4"
	fil2 = fil+"."+typ
	clip = VideoFileClip(fil2)
	  
	# getting subclip as video is large
	#clip = clip.subclip(55, 65)
	  
	# rotating clip by 45 degree
	clip = clip.rotate(90)
	  
	# showing clip
	#clip.ipython_display(width = 480)	
	
inp = []
rot(inp)
