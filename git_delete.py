exec(open('util.py').read())
def git_delete(inputs):
	from github import Github
	#git_delete([list_to_delete])
	token = load_data(["github_token.txt"])
	username = "github788788"
	repository = "code"
	g = Github(token)
	repo = g.get_repo(username+"/"+repository)
	to_delete = inputs[0]
	for a,val in enumerate(to_delete):
		file_to_delete = val
		print("file_to_delete = ",file_to_delete)
		file = repo.get_contents(file_to_delete)
		repo.delete_file(file_to_delete, "Delete file", file.sha)
		print(a,len(to_delete),file_to_delete+" deleted")

#inp = ["rea.py","rea2.py","rea3.py"]

if __name__=="__main__":
    #print("bark")
    #cwd = os.getcwd()
    #files = os.listdir(cwd)
    #git_commit([files])

	inp = []
	git_delete([inp])


"""
g = Github(token)
repo = g.get_repo(username+"/"+repository)
files_in_repo = repo.get_contents("")
pri(files_in_repo)
"""