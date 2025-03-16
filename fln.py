exec(open('util.py').read())
def fln(inp):
	dat = []
	dat.append([["was","arn"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["was","got"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["was","osl"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["was","cph"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["was","ber"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNCRVJwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["was","fra"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyBwgBEgNGUkFwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["was","par"],"https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNXF0anABggELCP___________wFAAUgBmAEC"])
	dat.append([["was","lon"],"https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAxIIL20vMHJoNmsSCjIwMjEtMDctMjhyDAgDEggvbS8wNGpwbHABggELCP___________wFAAUgBmAEC"])
	dat.append([["was","ice"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAhIIL20vMHJoNmsSCjIwMjItMDYtMjhyBwgBEgNLRUZwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["nyc","arn"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["nyc","got"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDR09UcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["nyc","osl"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDT1NMcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["nyc","cph"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["nyc","ber"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	dat.append([["nyc","fra"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["nyc","par"],"https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["nyc","lon"],"https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAxIJL20vMDJfMjg2EgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["nyc","ice"],"https://www.google.com/travel/flights/search?tfs=CBwQAhokag0IAxIJL20vMDJfMjg2EgoyMDIyLTA2LTI4cgcIARIDS0VGcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["bos","arn"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQVJOcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["bos","got"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["bos","osl"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDFjeF8SCjIwMjEtMDctMjhyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["bos","cph"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["bos","ber"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDQkVScAGCAQsI____________AUABSAGYAQI"])
	dat.append([["bos","fra"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIxLTA3LTI4cgcIARIDRlJBcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["bos","par"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDVxdGpwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["bos","lon"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDQk9TEgoyMDIxLTA3LTI4cgwIAxIIL20vMDRqcGxwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["bos","ice"],"https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDQk9TEgoyMDIyLTA2LTI4cgcIARIDS0VGcAGCAQsI____________AUABSAGYAQI"])
	dat.append([["par","arn"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDQtMDdyBwgBEgNBUk5wAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["par","got"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMjZyBwgBEgNHT1RwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["par","cph"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMzByBwgBEgNDUEhwAYIBCwj___________8BQAFIAZgBAg"])
	dat.append([["par","osl"],"https://www.google.com/travel/flights/search?tfs=CBwQAhojagwIAxIIL20vMDVxdGoSCjIwMjItMDMtMjZyBwgBEgNPU0xwAYIBCwj___________8BQAFIAZgBAg"])
	

	#fra arn https://www.google.com/travel/flights/search?tfs=CBwQAhojagcIARIDRlJBEgoyMDIyLTA3LTA3cgwIAxIIL20vMDZteHNwAYIBCwj___________8BQAFIAZgBAg
	#fra got https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDRlJBEgoyMDIyLTA3LTA3cgcIARIDR09UcAGCAQsI____________AUABSAGYAQI
	#fra cph https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDRlJBEgoyMDIyLTA3LTA3cgcIARIDQ1BIcAGCAQsI____________AUABSAGYAQI
	#fra osl https://www.google.com/travel/flights/search?tfs=CBwQAhoeagcIARIDRlJBEgoyMDIyLTA3LTA3cgcIARIDT1NMcAGCAQsI____________AUABSAGYAQI
	#
	usa = ["was","nyc","bos"]
	eur = ["arn","got","osl","cph","ber","fra","par","lon"]
	nor = ["arn","got","osl","cph","ber"]
	lis = []
	lis.append(["usa",usa])
	lis.append(["eur",eur])
	lis.append(["nor",nor])
	dep = whi("depart, match = usa,eur,nor")
	arr = whi("arrive, match = usa,eur,nor")
	print ("dep",dep)
	def spe(inp):
		loc = inp[0]
		lis = inp[1]
		for a,val in enumerate(loc):
			print("val",val)
			for b,val2 in enumerate(lis):
				if val==val2[0]:
					print("val2",val2)
					for c,val3 in enumerate(val2[1]):
						loc.append(val3)
					loc.pop(a)
					print("loc",loc)
		return loc
	dep = spe([dep,lis])
	arr = spe([arr,lis])
	print ("dep",dep)
	print ("arr",arr)
	
	lis = []
	url = []
	mis = []
	for a,val in enumerate(dep):
		for b,val2 in enumerate(arr):
			lis.append([val,val2])
	for a,val in enumerate(lis):
		hit = 0
		for b,val2 in enumerate(dat):
			if val in val2:
				print(val,val2)
				url.append(val2[1])
				hit =1
				break
		if hit==0:
			mis.append([val])
	dis(mis)
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
		

	
	
		"""
			# old fln codes..might be of use some day..inp = []
fln(inp)
		"""