
exec(open('util.py').read())
def tube(inp):

	from pytube import YouTube

	url = "https://www.youtube.com/watch?v=Nj77DsplDa4"

	try:
	   video = YouTube(url)
	   stream = video.streams.filter(only_audio=True).first()
	   #stream.download(filename=f"{video.title}.mp3")
	   stream.download(filename=f"{video.title}.mp4")
	   print("The video is downloaded in MP3")
	except KeyError:
	   print("Unable to fetch video information. Please check the video URL or your network connection")
	
inp = []
tube(inp)