exec(open('util.py').read())
def test4(inp):
	import subprocess

	url = "https://www.info33.pythonanywhere.com"  # Replace with your desired URL
	subprocess.run(["start", "chrome", "--incognito", url], shell=True)
	subprocess.run(["start", "chrome", "--incognito", url], shell=True)

inp = []
test4(inp)