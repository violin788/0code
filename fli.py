exec(open('util.py').read())
def fli(inp):
	
	sto = []
	sto.append(["was","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["was","got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["was","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["was","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["was","ber","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNCRVJwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["was","fra","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNGUkFwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["was","par","https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNXF0anABggELCP___________wFAAUgBmAEC"])
	sto.append(["was","lon","https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNGpwbHABggELCP___________wFAAUgBmAEC"])
	sto.append(["was","ice","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAhIIL20vMHJoNmsSCjIwMjItMDYtMjhyBwgBEgNLRUZwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["nyc","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["nyc","got","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDR09UcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["nyc","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDT1NMcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["nyc","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["nyc","ber","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	sto.append(["nyc","fra","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["nyc","par","https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["nyc","lon","https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["nyc","ice","https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIyLTA2LTI4cgcIARIDS0VGcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["bos","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["bos","got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["bos","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["bos","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["bos","ber","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	sto.append(["bos","fra","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["bos","par","https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["bos","lon","https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["bos","ice","https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIyLTA2LTI4cgcIARIDS0VGcAGCAQsI____________AUABSAGYAQI"])
	sto.append(["par","arn","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDQtMDdyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["par","got","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMjZyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["par","cph","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMzByBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	sto.append(["par","osl","https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMjZyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])	
	
	dep = whi3(["depart = "])
	arr = whi3(["arrive = "])
	#dep = ["was","nyc"]
	#arr = ["par","ber"]
	if "eur" in arr:
		arr = ["arn","got","osl","cph","ber","fra","par","lon"]

	gen = []
	url2 = []
	for a,val in enumerate(dep):
		for b,valb in enumerate(arr):
			app = [val,valb]
			for c,valc in enumerate(sto):
				mat1 = valc[0]
				mat2 = valc[1]
				if val==mat1:
					if valb==mat2:
						url = valc[2]
						url2.append(url)

	pri(url2)
	#num3(url2)
	num4([url2,2])
	for a,val in enumerate(url2):
		hod3(["ctrl","pageup",1,1])
		if a==len(url2)-2:
			break
	for a,val in enumerate(url2):
		cf_estt(["jul",0,0])
		if a==len(url2)-1:
			break
		hod3(["ctrl","pagedown",1,1])

inp = []
fli(inp)