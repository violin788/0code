exec(open('util.py').read())
def cpl(inp):
	"""
	https://www3.cs.stonybrook.edu/~alee/g++/g++.html
	https://www.tutorialspoint.com/How-to-compile-and-run-the-Cplusplus-program
	in terminal write "g++ to compile"
	then default file is a.exe, just type
	"a" or "a.exe" to run
	g++ -o wor wor.cpp
	g++ wor.cpp
	"""
	"""
	tex = "g++ -o wor wor.cpp"
	wri3([tex,2])
	key([["enter",1,0,2]])
	tex2 = "wor.exe"
	wri3([tex,1])
	key([["enter",1,0,0]])
	g++ -o wor wor.cpp
	
	#in order to run c++ code mingw,cygwin,vcpkg? cygwin install from
	berkley from file, install vcpkg to automate library install 
	#where iostream is located is
	E:\\MinGW\\lib\\gcc\\mingw32\\6.3.0\\include\\c++
	"""
	import subprocess
	gpf = "g++.exe"
	gpd = "E:\\MinGW\\bin"
	gpl = gpd+"\\"+gpf
	#fil = "wor2"
	fil =str(input("file = "))
	cod = fil+".cpp"
	sav = fil+".exe"
	print("compiling file "+cod+" to file "+sav)
	#try:
	subprocess.run([gpl,cod,"-o",sav])
	#except:
	#print("error..")
	#sye()
	tim1 = os.path.getmtime(sav)
	#from datetime import datetime
	now = datetime.datetime.now()
	tim2 = datetime.datetime.timestamp(now)
	dif = tim2 - tim1
	#print(tim1,tim2,dif)
	print("dif = ",dif)
	print(type(tim1),type(tim2))
	if dif>500:
		print("error..took "+str(int(dif))+" milliseconds")
		sye()
	else:
		print("success..comp time =  "+str(int(dif))+" milliseconds")
		sw2([sav,0])
	
inp = []
cpl(inp)