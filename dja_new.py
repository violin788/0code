exec(open('util.py').read())
exec(open('compile3.py').read())
cwd = os.getcwd()
def dja_new(inp):
	project_name =str(input("name of project/site = "))
	url_name =str(input("name of url in project = "))
	out = project_name+"___"+url_name
	write_data(["django_new.txt",out])
	compile3(["dja1.py"])
	shell(["dja1.pyc"])
	shutil.copy("dja_main.py",project_name+"\\"+project_name+"\\urls.py")
	compile3(["dja2.py"])
	shutil.copy("django_new.txt",project_name+"\\django_new.txt")
	shutil.copy("dja2.pyc",project_name+"\\dja2.pyc")
	time.sleep(2)

	click =str(input("click when you have manully run dja2.pyc in the new folder = "))
	
	shutil.copy("dja_code.py",project_name+"\\"+url_name+"\\views.py")

	text = load_data(["dja_url.py"])
	text2 = text.replace("members",url_name)
	#out_file = 
	dst = project_name+"\\"+url_name+"\\urls.py"
	write_data([dst,text2])

	file = project_name+"\\"+project_name+"\\urls.py"
	new_url_list = load_data([file])
	rep1 = "urlpatterns = ["
	rep2 = rep1+"\n"+"    path('', include('"+url_name+".urls')),"
	new_url_list2 = new_url_list.replace(rep1,rep2)
	dst2 = project_name+"\\"+project_name+"\\urls.py"
	print (new_url_list2)
	write_data([dst2,new_url_list2])
	#wri("cd..",2)
	#key([["enter",1,0,2]])
	print("done??")


inp = []
dja_new(inp)