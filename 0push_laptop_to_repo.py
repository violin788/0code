import os
import subprocess
import pytz
from datetime import datetime
os.chdir("c:\\Users\\--\\0code\\0code")
"""
specific = "main.py"
virginia_tz = pytz.timezone('America/New_York')
virginia_time = datetime.now(virginia_tz)
print("Virginia Time:", virginia_time)
now = datetime.now()
time_new = virginia_time.strftime("%Y-%m-%d %H:%M:%S") 
with open(specific, "r") as file:
    iden_start_time = "#last updated="
    iden_end_time = "----------"
    content = file.read()
    start_old_time_string = content.find(iden_start_time)
    end_old_time_string = content.find(iden_end_time)
    old_time_string = content[start_old_time_string:end_old_time_string]
    new_time_string = iden_start_time+str(time_new)
    content = content.replace(old_time_string,new_time_string)
    with open(specific, "w") as file:
        file.write(content)
print(specific,new_time_string)
"""

subprocess.run(["git", "status"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Your commit message"])
subprocess.run(["git", "push", "origin", "main"])
