exec(open('util.py').read())
#exec(open('git_commit.py').read())
"""
email
media788788@gmail.com,violin78@protonmail.com,cello34@protonmail.com,violin78@mail.com,usa2@email.com
code.7z

win8.1
C:\\Users\\--\\Downloads\\code.7z
win7
C:\\Users\\-\\Downloads\\code.7z

"""
import os
import getpass
cwd = os.getcwd()
download_directory = cwd.replace("code","Downloads")

def copy_to_other_partition():
	current_partition = get_current_partition()
	partition_list = get_partitions_by_size()
	largest_partition = partition_list[0][0]
	copy_to = ""
	if current_partition==largest_partition:
		copy_to = partition_list[1][0]
		print("copy to = "+str(copy_to))
	if current_partition!=largest_partition:
		copy_to = partition_list[0][0]
		print("copy to = "+str(copy_to))
	folder = copy_to+"Users"
	users_other_partition = os.listdir(folder)
	user_other_partition = users_other_partition[0]
	current_user = getpass.getuser()
	cwd = os.getcwd()
	code_directory_other_partition = cwd.replace(current_partition,copy_to)
	code_directory_other_partition = code_directory_other_partition.replace(current_user,user_other_partition)
	print(code_directory_other_partition)
	#copy all files from directory there?
	files = os.listdir(cwd)
	new_dir = code_directory_other_partition
	files_in_other_partition = os.listdir(new_dir)
	for a,val in enumerate(files_in_other_partition):
		try:
			os.remove(new_dir+"\\"+val)
		except:
			#shutil.rmtree(new_dir+"\\"+val)
			continue
	#end()

	for a,val in enumerate(files):
	    if "." in val:
	        src = cwd+"\\"+val
	        dst = new_dir+"\\"+val
	        try:
	        	shutil.copy(src,dst)
	        except:
	        	continue
	        print(a,len(files),"partiton copy",src,"to",dst)



#def save(inp):
naw = []
def generate_7z_file(inp):
	import py7zr
	cwd = os.getcwd()
	lis = os.listdir(cwd)
	#ski = if this in value in lis
	ski = [".exe"]
	#also get rid of, if does not contain.."."
	lis2 = []
	for a,val in enumerate(lis):
		no = 0
		for b,valb in enumerate(ski):
			if valb in val:
				no = 1
				break
		if no==1:
			continue
		if "." not in val:
			no=1
		if no==0:
			lis2.append(val)
	dri = dri_([])
	print(dri)
	acc = acc_([])
	#folder = cwd.replace("code","Downloads")
	code_file = download_directory+"\\code.7z"
	#dow = dri+"\\Users\\"+acc+"\\Downloads"
	#nam = cuf([])+".7z"
	#out = dow+"\\"+nam
	with py7zr.SevenZipFile(code_file,'w') as archive:
	    for a,val in enumerate(lis2):
	    	archive.write(val)
	    	cen = pro2([a,len(lis2),2])
	    	print(cen,end='\r')
	siz([code_file])
	time.sleep(1)
	
def email(inp):
	#click_logo2(["new_message.png"])
	click_logo4(["new_message4.png",2])
	emails = "media788788@gmail.com,violin78@protonmail.com,cello34@protonmail.com,violin78@mail.com,usa2@email.com"
	#copy_paste([emails])
	copy_paste2([emails,0])
	key([["tab",1,0,1]])
	#wri("code.7z",1)
	copy_paste2(["code.7z",0])
	click_logo4(["paperclip4.png",1])
	#cwd = os.getcwd()

	#folder = cwd.replace("code","Downloads")
	code_file = download_directory+"\\code.7z"
	#code_file = "C:\\Users\\-\\Downloads\\code.7z"	

	#copy_paste([code_file])
	copy_paste2([code_file,0])
	key([["enter",1,0,3]])
	click_logo4(["send4.png",3])

def update_github():
	import requests
	def get_repository_contents(username, repo_name):
	    url = f"https://api.github.com/repos/{username}/{repo_name}/contents"
	    response = requests.get(url)
	    if response.status_code == 200:
	        repo_contents = response.json()
	        return repo_contents
	    else:
	        print(f"Failed to fetch repository contents. Status code: {response.status_code}")
	        return None

	from github import Github
	access_token = load_data(["github_token.txt"])
	repository_name = 'code'
	g = Github(access_token)
	repo = g.get_user().get_repo(repository_name)
	contents = repo.get_contents("")

	files_in_repository = []
	for content in contents:
	    if content.type == "file":
	        files_in_repository.append(content.path)
	        #print(content.path)
	pri(files_in_repository)

	cwd = os.getcwd()
	files_in_cwd = os.listdir(cwd)
	pri(files_in_cwd)

	to_delete_from_repository = []
	for a,val in enumerate(files_in_repository):
		if val not in files_in_cwd:
			to_delete_from_repository.append(val)

	pri(to_delete_from_repository)
	from git_delete import git_delete
	print("now deleting from github files that were deleted")
	git_delete([to_delete_from_repository])

	to_create_in_respository = []
	for a,val in enumerate(files_in_cwd):
		if val not in files_in_repository:
			to_create_in_respository.append(val)
	from git_commit import git_commit
	print("now deleting from github files that were deleted")
	git_commit([to_create_in_respository])

	last_saved_file = "0last_edited.csv"
	last_saved_data = load_data([last_saved_file])
	check = []
	for a,val in enumerate(files_in_cwd):
		#print(val)
		modification_time = os.path.getmtime(val)
		formatted_last_modification_time = datetime.datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S.%f')
		new = []
		new.append(val)
		new.append(formatted_last_modification_time)
		print(new)
		check.append(new)
	update_in_github = []
	for a,val in enumerate(last_saved_data):
		for b,valb in enumerate(check):
			if val[0]==valb[0]:
				if val[1]!=valb[1]:
					if len(val[0])==1:
						continue
					update_in_github.append(val[0])
	print("update_in_github")
	pri(update_in_github)
	git_commit([update_in_github])

	write_data([last_saved_file,check])
	print("0last_edited.csv was created new")

input_generate_7z_file =str(input("generate 7z file? 1 for yes, blank for no = "))
input_email_to_self =str(input("email? 1 for yes, blank for no  = "))
inp = []
if input_generate_7z_file=="1":
	generate_7z_file(inp)
if input_email_to_self=="1":
	email([])
copy_to_other_partition()
update_github()
