exec(open('util.py').read())
def rum2web(inp):
	iframe_base = """
	<iframe frameborder="0" width="500" height="300" 
	src="https://rumble.com/embed/__rumble_code__/?pub=3i4h9q" 
	allowfullscreen="" loading="lazy" id="iquku"
	class="rumble">
    </iframe>
	"""
	embed_urls = []
	embed_urls.append("https://rumble.com/embed/v4spnbx/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4qvth5/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4rayvc/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4r928i/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4r4lq6/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4r43g9/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	embed_urls.append("https://rumble.com/embed/v4qyb7l/?pub=3i4h9q")

	embed_codes = []
	for a,val in enumerate(embed_urls):
		new = val.replace("https://rumble.com/embed/","")
		new = new.replace("/?pub=3i4h9q","")
		embed_codes.append(new)
	pri(embed_codes)

	iframe_htmls = []
	for a,val in enumerate(embed_codes):
		new = iframe_base.replace("__rumble_code__",val)
		iframe_htmls.append(new)
	pri(iframe_htmls)
	
	rum2web_out_file = ""
	for a,val in enumerate(iframe_htmls):
		rum2web_out_file = rum2web_out_file+val+"\n\n"
	out_file = "rumble_iframe_htmls.txt"
	write_data([out_file,rum2web_out_file])
	start_file([out_file,0])

	
inp = []
rum2web(inp)

"""
	https://rumble.com/embed/v4spnbx/?pub=3i4h9q
	https://rumble.com/embed/v4qvth5/?pub=3i4h9q
	https://rumble.com/embed/v4rayvc/?pub=3i4h9q
	https://rumble.com/embed/v4r928i/?pub=3i4h9q
	https://rumble.com/embed/v4r4lq6/?pub=3i4h9q
	https://rumble.com/embed/v4r43g9/?pub=3i4h9q
	https://rumble.com/embed/v4qvtai/?pub=3i4h9q
	https://rumble.com/embed/v4qyb7l/?pub=3i4h9q
	"""