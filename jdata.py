exec(open('util.py').read())
def json():

	import json

	# Open and load the JSON file
	with open('earn-feb-2025.json', 'r') as file:
	    data = json.load(file)

	# Now `data` contains the content of the JSON file
	print(data)
	
	
	
	
json()