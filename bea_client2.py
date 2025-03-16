exec(open('util.py').read())
def gdp2(inp):

	import datapungibea as dpb
	data = dpb.data("B1B06B4B-D6F8-492B-8FE4-352501E2652A")
	data.NIPA('T10101')
	
inp = []
gdp2(inp)