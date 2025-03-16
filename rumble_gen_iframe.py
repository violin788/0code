exec(open('util.py').read())
def rumble_gen_iframe(inp):
	base_iframe = """
<iframe frameborder="0" width="500" height="300" 
src="https://rumble.com/embed/___rumble_code___/?pub=3i4h9q" 
allowfullscreen="" loading="lazy" id="iquku"
class="rumble">
</iframe>
	"""	
	base_link = "<a href=\"___rumble_url___\">Link = ___rumble_url___</a>"


	#1st=title,2nd = embed url
	rumble_data = []
	rumble_data.append(["https://rumble.com/v4v6n4l-nevada-130-thousand-illegal-votes-were-cast-in-nevada.html","https://rumble.com/embed/v4spnbx/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tdnz8-arizona-explanation-of-voter-fraud.html","https://rumble.com/embed/v4qvth5/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tst7l-over-300000-ballot-images-lost-georgia-2020-recount-fulton-county.html","https://rumble.com/embed/v4rayvc/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tqwl6-georgia-joseph-rossi-georgia-recount-violated-georgia-election-law.html","https://rumble.com/embed/v4r928i/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tmg43-arizona-poll-worker-testifies-machine-switched-votes-from-trump-to-biden..html","https://rumble.com/embed/v4r4lq6/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tlxul-government-coruption-kt-mcfarland.html","https://rumble.com/embed/v4r43g9/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tdnsl-michigan-explanation-of-voter-fraud.html","https://rumble.com/embed/v4qvtai/?pub=3i4h9q"])
	rumble_data.append(["https://rumble.com/v4tg5ou-michigan-2020-electon-van-drops-of-ballots-in-middle-of-night.html","https://rumble.com/embed/v4qyb7l/?pub=3i4h9q"])
	
	out_text =""
	out_file ="rumble_iframes.txt"
	for a,val in enumerate(rumble_data):
		rumble_url = val[0]
		description = val[0]
		description = description.replace("https://rumble.com/","")
		description = description.replace(".html","")
		description = description[description.find("-"):len(description)]
		description = description.replace("-"," ")
		code = val[1]
		code = code.replace("https://rumble.com/embed/","")
		code = code.replace("/?pub=3i4h9q","")
		iframe = base_iframe.replace("___rumble_code___",code)
		#link = base_link.replace("___rumble_url___",rumble_url)
		out_text = out_text+description+"\n\n"+"Link = "+rumble_url+"\n\n"+rumble_url+"\n\n"+iframe+"\n\n"



	write_data([out_file,out_text])
	start_file([out_file,0])


	
inp = []
rumble_gen_iframe(inp)