#exec(open('util.py').read())
import os
def imp(inp):
	inp = inp
	#xlrd,pyautogui,xlwt,xlsxwriter,pandas
	ray = []
	"""
	const prompt = require('prompt-sync')({sigint: true});
	const shell = require('shelljs');
	const fs = require('fs'); 
	"""
	#ray.append("python -m pip install --upgrade pip")
	ray.append("prompt-sync")
	ray.append("shelljs")
	ray.append("fs")
	for a,val in enumerate(ray):
		print ("val",val)
		#command = val
		#if "python" not in val:
		command = "npm install "+str(val)
		os.system(command)
		#os.system("pip install "+val[1])


	#os.system("pip install xlrd")		
inp = []
imp(inp)