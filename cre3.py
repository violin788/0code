import os

file_name = input("Enter the name: ")
if not file_name.endswith(".py"):
    file_name += ".py"

with open(file_name, 'w') as f:
    f.write("exec(open('util.py').read())\n")
    f.write(f"def {file_name[:-3]}():\n\t\n\t\n\t\n")
    f.write(f"{file_name[:-3]}()")

os.system(f"start {file_name}")
