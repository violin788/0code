exec(open('util.py').read())
def face(inp):

	search = whi("search for? = ")
	alt3([1,1])
	for a,val in enumerate(search):
		print(a)
		#if a==0:
		#	alt(1,1)
		url1 = "https://www.facebook.com/marketplace/103795126325698/search?deliveryMethod=local_pick_up&sortBy=price_ascend&query="
		search2 = val
		url2 = "&exact=false"
		url = url1+search2+url2
			#if len(url)>3:
		single_url([url,0])	
		#command = "start \"\" "+url
		#os.system(command)
		#time.sleep(2)
		#time.sleep(3)


	
inp = []
face(inp)