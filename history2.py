exec(open('util.py').read())
def his2(inp):
		
	#!/usr/bin/env python

	try:
	    # For Python 3.0 and later
	    from urllib.request import urlopen
	except ImportError:
	    # Fall back to Python 2's urllib2
	    from urllib2 import urlopen

	import certifi
	import json

	def get_jsonparsed_data(url):
	    """
	    Receive the content of ``url``, parse it as JSON and return the object.

	    Parameters
	    ----------
	    url : str

	    Returns
	    -------
	    dict
	    """
	    response = urlopen(url, cafile=certifi.where())
	    data = response.read().decode("utf-8")
	    return json.loads(data)

	url = ("https://financialmodelingprep.com/api/v3/historical-price-full/index/%5EDJI?apikey=YOUR_API_KEY")
	print(get_jsonparsed_data(url))
	
inp = []
his2(inp)