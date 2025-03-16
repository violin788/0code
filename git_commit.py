exec(open('util.py').read())
def git_commit(inputs):
    #git_commit([files_to_send])
    input_file_list = inputs[0]
    from github import Github
    from github import UnknownObjectException
    # GitHub personal access token
    access_token = load_data(["github_token.txt"])
    repository_name = 'code'
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    contents = repo.get_contents("")

    files_to_upload = []
    for a,val in enumerate(input_file_list):
        if "0last_edited" in val:
            continue
        if "github" in val or "token" in val:
            continue
        if "git_commit" in val or "git_delete" in val:
            continue
        if "." not in val or ".pyc" in val:
            continue
        if ".xls" in val or ".csv" in val or ".png" in val or ".lnk" in val:
            continue
        files_to_upload.append(val) 
    pri(files_to_upload)
    for a,val in enumerate(files_to_upload):
        print(a,len(files_to_upload),val)
        file_path = val
        try:
            file_content = load_data([val])
        except:
            continue
        try:
            # Try to get the existing file
            existing_file = repo.get_contents(file_path)
            
            # Update the existing file
            repo.update_file(existing_file.path, "file updated! yo!", file_content, existing_file.sha)
            print("File updated successfully.")
        except UnknownObjectException:
            # If the file doesn't exist, create it
            repo.create_file(file_path, "file created! yo!", file_content)
            print("File created successfully.")


if __name__=="__main__":
    cwd = os.getcwd()
    files = os.listdir(cwd)
    git_commit([files])