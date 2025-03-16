exec(open('util.py').read())
def jav(inp):
	import js2py
	from js2py import require
	cod = rea4(["jav","js"])
	context = js2py.EvalJs(enable_require=True)
	context.eval(cod)
	
inp = []
jav(inp)