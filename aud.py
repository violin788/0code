exec(open('util.py').read())
#def aud(inp):
from moviepy.editor import *
#import moviepy
#inp = inp
fol = "C:\\Users\\-\\Downloads"
fil = "election"
fil = fil+".mp4"
out = ".mp3"
mp4 = fol+"\\"+fil
mp3 = mp4.replace("mp4","mp3")
print(mp4)
print(mp3)
vif = VideoFileClip(mp4)
auf = vif.audio
auf.write_audiofile(mp3)
vif.close()
auf.close()


#inp = []
#aud(inp)