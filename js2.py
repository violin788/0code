exec(open('util.py').read())
def js2(inp):
	import js2py
	javascript_code = load_data(["js2.txt"])
	js2py.eval_js(javascript_code)
inp = []
js2(inp)