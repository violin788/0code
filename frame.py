exec(open('util.py').read())
def frame(inp):
	
	import cv2
	directory = "C:\\Users\\-\\Downloads\\"
	file_name = "tennis"
	file = file_name+".mp4"
	file_location = directory+file
	vidObj = cv2.VideoCapture(file_location)
	frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT)) 
	fps = int(vidObj.get(cv2.CAP_PROP_FPS))
	print(frames,fps)
	for a in range(0,frames+1):
		output_file = file_name+str(a+1)+".jpg"
		
		vidObj.set(cv2.CAP_PROP_POS_FRAMES, a)
		ret, frame = vidObj.read()

		#cv2.imwrite(output_file, image)
		cv2.imwrite(output_file, frame)
		#cv2.imwrite('my_video_frame.png', frame)

		print(output_file)
	sye()

	
	length = int(cap. get(cv2. CAP_PROP_FRAME_COUNT))
	print( length )
	sye()
	count = 0
	success = 1
	new_directory = directory+file_name
	try:
		os.mkdir(new_directory)
	except:
		already = 1
	while success:
		count += 1
		success, image = vidObj.read()
		output_file = directory+new_directory+"\\"+file_name+"-"+str(count)+".jpg"
		print(output_file)
		try:
			cv2.imwrite(output_file, image)
		except:
			continue
		
inp = []
frame(inp)