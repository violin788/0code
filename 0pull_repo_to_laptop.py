import subprocess
import os

# Path to the Git lock file
git_lock_path = 'C:/Users/--/0code/.git/index.lock'

# Remove the lock file if it exists
if os.path.exists(git_lock_path):
    print(f"Removing existing lock file: {git_lock_path}")
    os.remove(git_lock_path)
# Your git commands
commands = [
    'git fetch --all',
    'git reset --hard origin/main'
]
# Run the commands
for cmd in commands:
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)
