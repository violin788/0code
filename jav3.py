exec(open('util.py').read())
def jav2(inp):
	"""
	import js2py
	from js2py import require
	cod = rea4(["jav3","js"])
	context = js2py.EvalJs(enable_require=True)
	context.eval(cod)
	"""
	import js2py
	#from js2py import require
	cod = rea4(["jav3","js"])

	#ctx = EvalJs(enable_require=True)
	#ctx.execute(cod)

	context = js2py.EvalJs(enable_require=True)
	context.eval(cod)
	


	#run = js2py.eval_js(cod)

	
inp = []
jav2(inp)