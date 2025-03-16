exec(open('util.py').read())
def mp4_mp3_2(inp):
	
	import subprocess
	import os

	def convert_mp4_to_mp3(input_file, output_file):
	    # Use ffprobe to get the audio stream information
	    ffprobe_command = ['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'default=noprint_wrappers=1:nokey=1', input_file]
	    ffprobe_output = subprocess.check_output(ffprobe_command, universal_newlines=True).strip()

	    # Check if the file has an audio stream
	    if 'audio' not in ffprobe_output:
	        print("Error: Input file does not contain an audio stream")
	        return

	    # Use lame to convert the audio stream to MP3
	    lame_command = ['lame', '--silent', input_file, output_file]
	    subprocess.run(lame_command)

	    print(f"Conversion completed. MP3 file saved as {output_file}")

	# Example usage
	input_file = 'input_video.mp4'
	output_file = 'output_audio.mp3'
	convert_mp4_to_mp3(input_file, output_file)
	
	
inp = []
mp4_mp3_2(inp)