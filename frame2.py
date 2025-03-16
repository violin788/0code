exec(open('util.py').read())
def frame2(inp):

	import cv2 
	  
	# Function to extract frames 
	#def FrameCapture(path): 
	  
	    # Path to video file 
    
	file = "C:\\Users\\-\\Downloads\\ukr1.mp4"
    vidObj = cv2.VideoCapture(file)
    sye()
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite("frame%d.jpg" % count, image) 
  
        count += 1

	
inp = []
frame2(inp)