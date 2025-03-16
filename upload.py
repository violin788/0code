exec(open('util.py').read())
def upload(inp):

	mp4_file_name = "fulton_300k_votes"
	description = "Over 300,000 ballot images lost Georgia 2020 recount (Fulton county)"

	media_file = mp4_file_name
	if ".mp4" not in mp4_file_name:
		media_file = mp4_file_name+".mp4"
	files = []
	files.append([media_file,description])	
	cwd = os.getcwd()
	downloads_directory = cwd.replace("code","Downloads")	
	rumble_url = "https://rumble.com/upload.php"
	twitter_url = "https://twitter.com/compose/post"
	#alt_win81(["Chrome"]):
	alt_win81(["Chrome",1])
	for a,val in enumerate(files):
		file_name = val[0]
		file_title = val[1]
		hold_button(["ctrl","t",1,1])
		copy_paste2([rumble_url,1])
		key([["enter",1,0,5]])
		click_logo4(["rumble_upload_button.png",3])
		file_to_upload = downloads_directory+"\\"+file_name
		print(file_to_upload)
		copy_paste2([file_to_upload,1])
		key([["enter",1,0,2]])
		key([["tab",1,0,2]])
		copy_paste2([file_title,1])

		#upload to twitter
		hold_button(["ctrl","t",1,1])
		copy_paste2([twitter_url,2])
		key([["enter",1,0,5]])
		copy_paste2([file_title,2])
		click_logo4(["twitter_upload_button.png",3])
		copy_paste2([file_to_upload,1])
		key([["enter",1,0,2]])
		click_logo4(["rumble_upload_button.png",3])

	
inp = []
upload(inp)