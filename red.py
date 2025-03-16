exec(open('util.py').read())
def red(inp):
	"""
	import pyperclip	
	url = "https://old.reddit.com/user/savant78/submitted/?sort=new"
	single_url([url,1])
	time.sleep(3)
	hod3(["ctrl","a",1,1])
	hod3(["ctrl","c",1,1])
	# Read the text from the clipboard
	text = pyperclip.paste()
	"""
	text = load_data(["red1.txt"])
	posts = []
	quit = 0
	iden_start = "submitted"
	iden_end = "comment"
	search_from = 0
	while(quit<1):
		begin_line = text.find(iden_start,search_from)
		end_line = text.find(iden_end,begin_line)
		if end_line<0:
			quit=1
			break
		if end_line<begin_line:
			quit=1
			break			
		line = text[begin_line:end_line]
		posts.append(line)
		print(begin_line,end_line,line)
		search_from = end_line

	from datetime import datetime
	now = datetime.now()
	current_hour = now.strftime("%H")
	sure = int(current_hour)-1
	start = "submitted"
	end = "\n"
	post2 = []
	for a,val in enumerate(posts):
		new_val = val[val.find(start):val.find(end)]
		if "day ago" in new_val:
			continue
		if "days ago" in new_val:
			continue
		category = new_val[new_val.find("r/"):len(new_val)]
		category = category.replace("\r","")
		category = category.replace("r/","")
		category = category.lower()
		if len(category)==0:
			continue
		how_long_ago = new_val[0:new_val.find("ago by")]
		how_long_ago = how_long_ago.replace("submitted ","")
		if "dupvoteddownvotedhidde" in how_long_ago:
			continue
		if "hour" in how_long_ago:
			hours_ago = how_long_ago[0:how_long_ago.find(" ")]
			hours_ago = int(hours_ago)
			if hours_ago>sure:
				continue
		#how_long_ago = how_long_ago.replace(" ","")
		more = [category,how_long_ago]
		post2.append(more)
	post2.sort()
	pri(post2)
	out_text = ""
	for a,val in enumerate(post2):
		out_text = out_text+str(val)+"\n"
	#post2 = post2.sort()
	#post2.sort(key=lambda x:x[0],reverse=False)
	out_file = "red2.txt"
	write_data([out_file,out_text])
	start_file([out_file,0])

	
inp = []
red(inp)