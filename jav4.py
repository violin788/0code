exec(open('util.py').read())
def jav4(inp):
	"""
	import js2py
	from js2py import require
	cod = rea4(["jav4","js"])
	js2py.eval_js(cod)
	#context = js2py.EvalJs(enable_require=True)
	#context.eval(cod)
	"""
	#subprocess.Popen(['notepad.exe', lo])
	import js2py
	from js2py import require
	
	nod = 'C:\\Program Files\\nodejs\\node.exe'
	jav = 'C:\\Program Files\\nodejs\\jav4.js'

	subprocess.Popen([nod,jav])
	



inp = []
jav4(inp)