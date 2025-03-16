exec(open('util.py').read())
def rumble_gen(inp):


	vid_code = """

	<div class="gjs-grid-column">
	        <iframe id="__iframe_id__" src="https://rumble.com/embed/__vid_code__/?pub=3i4h9q"></iframe>
	</div>


	"""

	row_code = """

	        <div id="__state_row__" class="gjs-grid-row">
	                <div id="__state_col__" class="gjs-grid-column">
	                        <div id="__state_name__">__state__</div>
	                </div>
	                <div id="__vid_col__" class="gjs-grid-column">
	                        <div id="__vid_row__" class="gjs-grid-row">

									<div class="gjs-grid-column">
									        <iframe id="__iframe_id__" src="https://rumble.com/embed/__vid_code__/?pub=3i4h9q"></iframe>
									</div>

									<div class="gjs-grid-column">
									        <iframe id="__iframe_id__" src="https://rumble.com/embed/__vid_code__/?pub=3i4h9q"></iframe>
									</div>
									
										                                <div class="gjs-grid-column">
	                                        <div id="irpeg"><iframe id="__vid3__"
	                                                        src="https://rumble.com/embed/__vid3_code__/?pub=3i4h9q"
	                                                        id="__vid3__"></iframe></div>
	                                </div>
	                        </div>
	                </div>
	        </div>
	"""
	"""
	new_code = row_code
	new_code = new_code.replace("__state_row__",valb[0]+"_row_"+str(b))
	new_code = new_code.replace("__state_row__",valb[0]+"_row_"+str(b))
	new_code = new_code.replace("__state__",valb[0])
	new_code = new_code.replace("__state_row__",valb[0]+"_row_"+str(b))
	"""
	css_code = """

	        #__vid_id__ {
	                width: 400px;
	                height: 300px;
	        }
	"""

	rumble_urls = []

	#<iframe src="https://rumble.com/embed/v4spnbx/?pub=3i4h9q"></iframe>
	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)

	new = []
	new.append("arizona")
	new.append("lankford")
	new.append("us senator")
	new.append("130 thousand illegal votes were cast in Nevada")
	new.append("https://rumble.com/embed/v4spnbx/?pub=3i4h9q")
	new.append("https://rumble.com/v4v6n4l-nevada-130-thousand-illegal-votes-were-cast-in-nevada.html")
	#<a href="https://rumble.com/embed/v4spnbx/?pub=3i4h9q">Link = "https://rumble.com/embed/v4spnbx/?pub=3i4h9q"</a>
	rumble_urls.append(new)

	new = []
	new.append("georgia")
	new.append("Joseph Rossi")
	description = """
	Georgia Recount Violated Georgia Election Law
	"""
	new.append(description)
	embed_url = """
	https://rumble.com/embed/v4qyb7l/?pub=3i4h9q
	
	"""
	new.append(embed_url)
	rumble_url = """
	__rumble_url__
	"""
	new.append(rumble_url)
	rumble_urls.append(new)

	new = []
	new.append("arizona")
	new.append("Abe Hamadeh")
	description = """
	Georgia Recount Violated Georgia Election Law
	"""
	new.append(description)
	embed_url = """
	https://rumble.com/embed/v4qyb7l/?pub=3i4h9q
	
	"""
	new.append(embed_url)
	rumble_url = """
	__rumble_url__
	"""
	new.append(rumble_url)



	new.append("Georgia Recount Violated Georgia Election Law")
	new.append("https://rumble.com/embed/v4r928i/?pub=3i4h9q")
	rumble_urls.append(new)

	#<iframe id="georgia1" src="https://rumble.com/embed/v4r928i/?pub=3i4h9q"></iframe>

	new = []
	new.append("georgia")
	new.append("??")
	new.append("Over 300,000 ballot images lost Georgia 2020 recount (Fulton county)")
	new.append("https://rumble.com/embed/v4rayvc/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("michigan")
	new.append("??")
	description = """
	Van Drops of Ballots in Middle of Night
	"""
	new.append(description)
	embed_url = """
	https://rumble.com/embed/v4qyb7l/?pub=3i4h9q
	"""
	rumble_urls.append(new)

	new = []
	new.append("michigan")
	new.append("Jim Runestad")
	new.append("(R) Michigan State Senator")
	new.append("Explanation of Voter Michigan Fraud")
	new.append("https://rumble.com/embed/v4qvtai/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("nevada")
	new.append("Lankford")
	new.append("130 thousand illegal votes were cast in Nevada")
	new.append("https://rumble.com/embed/v4spnbx/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("arizona")
	new.append("??")
	new.append("Explanation of Voter Fraud")
	new.append("https://rumble.com/embed/v4qvth5/?pub=3i4h9q")
	rumble_urls.append(new)

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)

	new = []
	new.append("__state__")
	new.append("__person__")
	new.append("__description__")
	new.append("__rumble_embed_url__")
	rumble_urls.append(new)


	#rumble_urls.sort()
	"""
	for a,val in enumerate(rumble_urls):
		new_code = row_code
		state = val[0]
		new_code.replace("__state_row__",state+"row")
	"""

	new_array = []
	for a,val in enumerate(rumble_urls):
		check = val[0]
		if "__state__" in check:
			continue
		match = 0
		for b,valb in enumerate(new_array):
			if check in valb[0]:
				match=1
				valb.append(val)
				break
		if match==0:
			new_array.append([check,val])

	pri(new_array)

	for a,val in enumerate(new_array):
		more_code = ""
		more_code = more_code+"""

		"""

	end()


	
inp = []
rumble_gen(inp)