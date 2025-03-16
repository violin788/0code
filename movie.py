exec(open('util.py').read())
def movie(inp):
	
	from moviepy.editor import VideoFileClip, concatenate_videoclips

	# Load video clips

	file1 = ""
	file2 = ""

	clip1 = VideoFileClip("C:\\Users\\--\\Downloads\\corrupt.mp4")
	clip2 = VideoFileClip("C:\\Users\\--\\Downloads\\election.mp4")

	# Concatenate video clips
	final_clip = concatenate_videoclips([clip1, clip2])

	# Save the final concatenated clip to a file
	final_clip.write_videofile("C:\\Users\\--\\Downloads\\0final.mp4")
		
	
inp = []
movie(inp)