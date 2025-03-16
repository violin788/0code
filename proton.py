exec(open('util.py').read())
def proton(inp):
	
	from protonmail_api import ProtonMailApi
	import base64

	# Initialize the ProtonMail API client
	api = ProtonMailApi(
	    username='violin78',
	    password='viovio',
	    api_url='https://api.protonmail.ch',
	    session=None  # You can provide a custom session if needed
	)

	# Log in to your ProtonMail account
	api.auth()

	# Compose the email with attachment
	message = {
	    'To': 'recipient@example.com',
	    'Subject': 'Hello from ProtonMail API with Attachment',
	    'Body': 'This is a test email sent using the ProtonMail API with an attachment!',
	    'Attachments': [{
	        'Name': 'example_attachment.txt',  # Name of the attachment
	        'Data': base64.b64encode(open('path_to_your_file/example_attachment.txt', 'rb').read()).decode(),  # Base64 encoded file data
	        'MimeType': 'text/plain'  # Mime type of the attachment
	    }]
	}

	# Send the email with attachment
	api.send_email(message)

	# Log out when done (optional)
	api.logout()	
	
inp = []
proton(inp)