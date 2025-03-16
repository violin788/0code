exec(open('util.py').read())
def replit(inp):
	

	import requests

	# Replace these values with your own Replit credentials and file path
	replit_username = "media788788@gmail.com"
	replit_password = "Medmed1!"
	file_path = "tes.txt"

	# Authenticate with Replit
	login_url = "https://replit.com/login"
	session = requests.Session()
	login_data = {
	    "username": replit_username,
	    "password": replit_password,
	}
	session.post(login_url, data=login_data)

	# Upload file
	upload_url = f"https://replit.com/{replit_username}/_share/upload"
	with open(file_path, "rb") as file:
	    files = {"file": (file_path, file)}
	    response = session.post(upload_url, files=files)

	if response.ok:
	    print("File uploaded successfully!")
	else:
	    print("Error uploading file.")
	
	
inp = []
replit(inp)