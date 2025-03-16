exec(open('util.py').read())
def rumble(inp):
	
	import requests

	# Replace these variables with your actual API credentials
	API_KEY = 'your_api_key'
	API_SECRET = 'your_api_secret'

	# URL for Rumble's API endpoint for video uploads
	UPLOAD_URL = 'https://api.rumble.com/videos'

	# Path to the video file you want to upload
	VIDEO_PATH = 'path/to/your/video.mp4'

	# Open the video file
	with open(VIDEO_PATH, 'rb') as file:
	    # Prepare the data for the request
	    files = {'file': file}
	    headers = {'Authorization': f'Bearer {API_KEY}:{API_SECRET}'}
	    
	    # Send the request to upload the video
	    response = requests.post(UPLOAD_URL, files=files, headers=headers)

	# Check if the upload was successful
	if response.status_code == 201:
	    print('Video uploaded successfully!')
	    # You can parse the response for additional information
	    print('Video ID:', response.json()['id'])
	else:
	    print('Failed to upload video. Error:', response.text)
	
	
inp = []
rumble(inp)