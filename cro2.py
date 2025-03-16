exec(open('util.py').read())
def cro(inp):
	
	sit =str(input("nav? = "))
	if ".com" not in sit:
		sit = "https://www.google.com/search?client=firefox-b-1-d&q="+sit

	pro = "E:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	sw(pro,3)

	htb("ctrl","shift","n",1,3)
	alt(1,1)
	af4(1,1)


	url = []
	url.append("www.croxyproxy.com")

	alt(1,1)
	

	num4([url,4])

	wri(sit,2)

	key([["enter",1,0,0]])


inp = []
cro(inp)