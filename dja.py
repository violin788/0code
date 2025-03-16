exec(open('util.py').read())
def dja(inp):

	project_name =str(input("name of project to start = "))
	port = 8000
	url = "http://localhost:"+str(port)+"/members"
	command = "start "+url
	os.system(command)
	#app.run(debug=True, port=port)
	command = "py "+project_name+"\\manage.py runserver"
	os.system(command)



inp = []
dja(inp)