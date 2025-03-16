exec(open('util.py').read())
def vot(inp):
	
	lis = []
	lis.append("Arizona")
	lis.append("Georgia")
	lis.append("Wisconsin")
	lis.append("Nevada")
	lis.append("Pennsylvania")
	lis.append("Michigan")

	out = []
	goo = []
	goo_url = "https://www.google.com/search?q="
	wik = []
	wik_url = "https://en.wikipedia.org/wiki/2020_United_States_presidential_election_in_"

	for a,val in enumerate(lis):
		spe = val+" nov 3 vote drop"
		out.append(spe)
		goo2 = goo_url+spe
		goo.append(goo2)
		wik2 = wik_url+val
		wik.append(wik2)
	pri(out)
	pri(goo)
	pri(wik)

inp = []
vot(inp)