exec(open('util.py').read())
#def aud2(inp):

import os
import sys
#from moviepy.editor import VideoFileClip
from moviepy import *
from moviepy.editor import VideoFileClip

dri = dri_([])
acc = acc_([])

dow = dri+":\\Users\\"+acc+"\\Downloads"
mp4 = dow+"\\aud.mp4"
video = VideoFileClip("example.mp4")


import ssl
print(ssl.OPENSSL_VERSION_INFO)


"""
#from moviepy.editor import *
import moviepy

dri = dri_([])
acc = acc_([])

dow = dri+":\\Users\\"+acc+"\\Downloads"
mp4 = dow+"\\aud.mp4"

print(mp4)




# Load the mp4 file
video = VideoFileClip("example.mp4")

# Extract audio from video
video.audio.write_audiofile("example.mp3")

	
#inp = []
#aud2(inp)
"""