import os,sys
import subprocess, pytz
from datetime import datetime
import pytz

def run_git_command(command):
    """Run a Git command and return its output, printing each line as it occurs."""
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in result.stdout:
        print(line.strip())  # Print real-time output for each line
    for line in result.stderr:
        print(line.strip())  # Print real-time error output if any
    result.wait()
    if result.returncode != 0:
        print(f"Error: {result.stderr.read()}")
        return None
    return result.stdout

def git_push():
    """Push changes to the GitHub repository with real-time progress feedback."""
    # Check if Git is initialized
    status = run_git_command(["git", "status"])
    if "fatal: not a git repository" in status:
        print("Git repository not initialized. Initializing...")
        run_git_command(["git", "init"])
    
    # Set remote repository URL (replace with your GitHub repository URL)
    remote_url = "https://github.com/violin788/0code.git"
    remote_check = run_git_command(["git", "remote", "get-url", "origin"])
    if remote_check is None:
        print(f"Setting remote URL: {remote_url}")
        run_git_command(["git", "remote", "add", "origin", remote_url])

    # Stage all changes
    print("Staging changes...")
    run_git_command(["git", "add", "."])

    virginia_tz = pytz.timezone('America/New_York')
    virginia_time = datetime.now(virginia_tz)
    string_time = virginia_time.strftime("%Y-%m-%d %H:%M:%S") 

    # Commit changes
    commit_message = "updated: "+string_time
    print(f"Committing with message: {commit_message}")
    run_git_command(["git", "commit", "-m", commit_message])

    # Force push changes to the main branch (overwrite remote)
    print("Force pushing changes to GitHub...")
    push_output = run_git_command(["git", "push", "--force", "origin", "main"])
    if push_output:
        print(push_output)
        print("Changes pushed successfully.")

#if __name__ == "__main__":
git_push()

virginia_tz = pytz.timezone('America/New_York')
virginia_time = datetime.now(virginia_tz)
string_time = virginia_time.strftime("%Y-%m-%d %H:%M:%S") 
file_main = 'main.py'
iden_time_begin = "#last updated="
iden_time_end = "----------"
with open(file_main, 'r') as file:
    content = file.read()
start_time = content.find(iden_time_begin)
if start_time<0:
    print("!!!!!!!")
    print("cannot find last updated begin identifier")
    print("you must make this findable, otherwise")
    print("whole file would be deleted.. = bad")
    print("!!!!!!!")
    sys.exit()
end_time = content.find(iden_time_end)
time_old = content[start_time:end_time]
time_new = iden_time_begin+string_time
content=content.replace(time_old,time_new)
with open(file_main, 'w') as file:
    file.write(content)
print(file_main+" save time updated!")
#format of laste updated = 
#"#last updated=2025-04-03 14:22:53----------"