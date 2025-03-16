exec(open('util.py').read())
def js(inp):
	import js2py
	javascript_code = load_data(["js.txt"])
	js2py.eval_js(javascript_code)
inp = []
js(inp)