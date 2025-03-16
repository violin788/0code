exec(open('util.py').read())
def fix(inp):
	cwd = os.getcwd()
	fea =cwd 
	lis = os.listdir(fea)
	inc = 0
	for a,val in enumerate(lis):
		if ".py" in val:
			try:
				tex = rea4([val,""])
			except:
				continue
			#but3([["enter","esc"],0,0])
			ide = "but3"
			if ide in tex:
				inc = inc+1
				print (inc, val)

				continue
				
				end = 0
				beg = 0
				while(end<1):
					loc1 = tex.find(ide,beg)
					if loc1<0:
						break
					loc2 = tex.find("\n",loc1)
					lin = tex[loc1:loc2]
					#hod3(["alt","tab",1,1)
					lin2 = lin.replace("num(","num4([")
					lin2 = lin2.replace(")","])")
					tex = tex.replace(lin,lin2)
					beg = loc1+1
				out = val.replace(".py","")
				wrt2([tex,out,"py"])
				print(out)
				sye()
			
inp = []
fix(inp)