exec(open('util.py').read())
def flask_gen(inp):
	
	array = []
	array.append(["__main__","client.html"])
	array.append(["cia","cia.html"])	
	#array.append(["contact","contact.html"])

	new_site_python = """
exec(open('util.py').read())
from flask import Flask
app = Flask(__name__)
"""
	for a,val in enumerate(array):
		portion = val[0]
		html_file = val[1]
		if "__main__" in portion:
			new_site_python = new_site_python+"@app.route('/')\n"
		if "__main__" not in portion:	
			new_site_python = new_site_python+"@app.route('/"+portion+"')\n"
		new_site_python = new_site_python+"def "+portion+"():\n"	
		new_site_python = new_site_python+"\thtml_code=\"\"\"\n"
		#make it so that it loads flask_gen.txt with stuff that is to be replaced..
		html_to_add = load_data([html_file])
		new_site_python = new_site_python+html_to_add+"\n"
		new_site_python = new_site_python+"\"\"\"\n\treturn html_code\n"
	new_site_python = new_site_python+"""
if __name__=='__main__':
   port = 5000
   url = "http://localhost:"+str(port)+"/"
   command = "start "+url
   os.system(command)
   app.run(debug=True, port=port)
       """
	write_data(["flask_new.py",new_site_python])
	os.startfile("flask_new.py")
	shell(["python flask_new.py"])

inp = []
flask_gen(inp)

