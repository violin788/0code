
import subprocess

# Path to the executable you want to run
exe_path = "C:\\Users\\--\\Desktop\\SpaceFinder.exe"

# Define the password (not secure, do not use in production)
password = ""

# Run the exe as Administrator using the password (not secure)
subprocess.run(['runas', '/user:Administrator', f'/password:{password}', exe_path])


