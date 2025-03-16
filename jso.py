exec(open('bas2.py').read())
def jso(inp):
	import json
	import numpy as np
	fil = 'iex.json'
	data = js2([fil])
	for a,val in data.items():
		sym = a
		clo = data[a]['chart'][0]['close']
		vol = data[a]['chart'][0]['volume']
		#print (data[a]['chart'][0]['close'])
		print (sym,clo,vol)
	sye()
	"""
	for a, val in data.items():
	   # if str(value).startswith('bo'):
	   for b,val2 in val.items():
	   	print (a,b,val2)
	   	print ("")
		#print(a, val)  # 👉️ website bobbyhadz.com
		#print (type(val))

	sye()
	print (len(data.items()))
	sye()
	print (len(data))
	for a, val in enumerate(data):
		print (data.items())
		#print (data[a].value())
	sye()
	"""
	for a, val in enumerate(data):
		print (val.items)\
		#print (data["PG"]['chart'][0]['close'])
		#print (data["PG"]['chart'][0]['volume'])
	sye()
	ray = []
	a = -1
	for values in data.values():
		a = a+1
		print(a,values)
		ray.append(values)
	sye()

	
    #dat2 = list(data.items())
	#print (dat2)
	print (dat2[0][1])
	print (type(dat2[0][1]))
	"""
	sye()

	dat3 = np.array(dat2)
	ray = list(data)
	#print(dat3)
	print(dat3[0])
	print(type(dat3[0]))
	#print(ray)
	sye()

	with open(fil, 'r') as f:
		data = json.load(f)

	print (data)
	data = json.load(fil)
	sye()
	f = open('iex.json')
	# returns JSON object as 
	# a dictionary
	data = json.load(f)
	print (data)
	print (data[0])
	sye()
	"""
inp = []
jso(inp)