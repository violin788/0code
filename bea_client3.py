exec(open('util.py').read())
def gdp3(inp):
	
	import requests
	import pandas as pd
	import config   ## File with API key

	# Components of request
	base = f'https://apps.bea.gov/api/data/?&UserID={config.bea_key}'
	dset = '&method=GetData&datasetname=NIPA'
	tbl = 'T20306' # Real PCE by Major Type of Product: NIPA Table 2.3.6.
	freq = '&Frequency=Q'
	yr = ','.join(map(str, range(2000, 2021)))
	fmt = '&ResultFormat=json'
	url = f'{base}{dset}&TableName={tbl}{freq}&Year={yr}{fmt}'

	# Request data
	r = requests.get(url).json()['BEAAPI']['Results']



inp = []
gdp3(inp)