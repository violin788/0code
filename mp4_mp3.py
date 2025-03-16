exec(open('util.py').read())
#def aud(inp):

from pydub import AudioSegment
from pydub.utils import mediainfo

def convert_mp4_to_mp3(video_path, output_path):
    # Load the MP4 video file
    audio = AudioSegment.from_file(video_path, format="mp4")

    # Get the audio codec and channels from the original video
    audio_codec = mediainfo(video_path)['codec_name']
    channels = mediainfo(video_path)['channels']

    # Export the audio as MP3
    audio.export(output_path, format="mp3", codec="libmp3lame", parameters=["-ac", str(channels)])

# Example usage
#input_file = 'input_video.mp4'
fol = "C:\\Users\\--\\Downloads"


cwd = os.getcwd()
download_directory = cwd.replace("code","Downloads")
print(download_directory)
end()


fil = "tennis"
fil = fil+".mp4"
input_file = fol+"\\"+fil
output_file = input_file.replace(".mp4",".mp3")
#output_file = 'output_audio.mp3'
convert_mp4_to_mp3(input_file, output_file)




"""
from moviepy.editor import *
#import moviepy
#inp = inp
fol = "C:\\Users\\-\\Downloads"
fil = "tennis"
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
"""

#inp = []
#aud(inp)