exec(open('util.py').read())
def frame3(inp):
	import cv2
	def get_num_frames(video_path):
	    # Open the video file
	    cap = cv2.VideoCapture(video_path)
	    # Get the total number of frames
	    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	    # Release the video capture object
	    cap.release()
	    return num_frames
	# Example usage
	#video_path = 'input_video.mp4'
	#mp4 location?
	video_path = "C:\\Users\\--\\Downloads\\tennis.mp4"
	num_frames = get_num_frames(video_path)
	print("Number of frames:", num_frames)
	def save_frame(video_path, output_path, frame_number):
	    # Open the video file
	    cap = cv2.VideoCapture(video_path)
	    # Set the frame position
	    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
	    # Read the frame
	    ret, frame = cap.read()
	    if ret:
	        # Save the frame as an image
	        cv2.imwrite(output_path, frame)
	        print(f"Frame {frame_number} saved as {output_path}")
	    else:
	        print("Error: Could not read frame")
	    # Release the video capture object
	    cap.release()
	# Example usage
	#video_path = "C:\\Users\\--\\Downloads\\tennis.mp4"

	#num_frames is max number of frames?
	#num_frames
	for a in range(1980,2100):
		frame_number = a  # Specify the frame number you want to save
		output_path = "C:\\Users\\--\\Downloads\\tennis-frame-"+str(frame_number)+".jpg"
		save_frame(video_path, output_path, frame_number)
		print(output_path)

inp = []
frame3(inp)