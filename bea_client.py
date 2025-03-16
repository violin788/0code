exec(open('util.py').read())
def gdp(inp):
		
	from pprint import pprint
	from pybea.client import BureauEconomicAnalysisClient
	#B1B06B4B-D6F8-492B-8FE4-352501E2652A
	# Initalize the new Client.
	bea_client = BureauEconomicAnalysisClient(api_key='B1B06B4B-D6F8-492B-8FE4-352501E2652A')

	# Grab the Dataset List.
	#dataset_list = bea_client.get_dataset_list()
	dataset_list = bea_client.get_dataset_list()
	pprint(dataset_list)

inp = []
gdp(inp)