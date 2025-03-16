exec(open('util.py').read())
def tls(inp):

	import ssl
	import urllib3

	ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
	# set other SSLContext options you might need
	response = urllib3.urlopen(url, context=ctx)
	
inp = []
tls(inp)