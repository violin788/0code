exec(open('util.py').read())
def free(inp):

	sea =str(input("search for = "))

	#https://fredericksburg.craigslist.org/search/zip?query=_____

	url = ["https://fredericksburg.craigslist.org/search/zip"]
	url.append("https://www.facebook.com/marketplace/103795126325698/free/")

	pri(url)
	num4([url,2])

inp = []
free(inp)