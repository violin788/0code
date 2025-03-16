exec(open('util.py').read())
def fli2(inp):
	
	dat = []
	dat.append(["was","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["was","got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["was","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["was","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["was","ber","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNCRVJwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["was","fra","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNGUkFwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["was","par","https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNXF0anABggELCP___________wFAAUgBmAEC"])
	dat.append(["was","lon","https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNGpwbHABggELCP___________wFAAUgBmAEC"])
	dat.append(["was","ice","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAhIIL20vMHJoNmsSCjIwMjItMDYtMjhyBwgBEgNLRUZwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["nyc","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["nyc","got","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDR09UcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["nyc","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDT1NMcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["nyc","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["nyc","ber","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	dat.append(["nyc","fra","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["nyc","par","https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["nyc","lon","https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["nyc","ice","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIyLTA2LTI4cgcIARIDS0VGcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["bos","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["bos","got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["bos","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["bos","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["bos","ber","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	dat.append(["bos","fra","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["bos","par","https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["bos","lon","https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["bos","ice","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIyLTA2LTI4cgcIARIDS0VGcAGCAQsI____________AUABSAGYAQI"])
	dat.append(["par","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDQtMDdyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["par","got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMjZyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["par","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMzByBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append(["par","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMjZyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])	

	eur = ["arn","got","osl","cph","ber","fra","par"]
	nor = ["arn","got","osl","cph"]

	dep = whi2(["depart"])
	arr = whi2(["arrive"])

	che = [dep,arr]
	for a,val in enumerate(che):
		if "eur" in val:
			che[a] = eur
		if "nor" in val:
			che[a] = nor

	dep = che[0]
	arr = che[1]
	url = []
	print(dep,arr)
	for a,val in enumerate(dat):
		for b,val2 in enumerate(dep):
			if val[0]==val2:
				for c,val3 in enumerate(arr):
					if val[1]==val3:
						url.append(val[2])

	pri(url)
	num4([url,1])
	for a,val in enumerate(url):
		if a==0:
			for b,val2 in enumerate(url):
				hod3(["ctrl","f",1,1])
				wri("economy",1)
				but(["esc"],0,0)
				but(["tab"],0,0)
				but(["tab"],0,0)
				but(["tab"],0,0)
				but(["tab"],0,0)
				if b<len(url)-1:
					hod3(["ctrl","pagedown",1,1])
				if b==len(url)-1:
					pgu(len(url),1)

	for a,val in enumerate(mis):
		val = val[0]
		print (val)
		#sye()
		url = ["https://www.google.com/travel/flights?tfs=CBwQARoaagwIAhIIL20vMHJoNmsSCjIwMjItMDUtMDhwAYIBCwj___________8BQAFIAZgBAg"]
		dep = val[0]
		arr = val[1]
		num4([url,5])
		hod3(["shift","tab",1,1])
		wri(dep,1)
		key([["tab",1,0,1]])
		wri(arr,1)
		key([["enter",2,1,0]])
		
inp = []
fli2(inp)