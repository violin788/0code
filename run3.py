exec(open('util.py').read())
def run3(inp):
	pas = []
	tex = ""
	end = len(inp)-1
	end = 0
	hit = 0
	fir = 0
	for a,val in enumerate(inp):
		if len(val)==1:
			if fir==0:
		#if a==0:
				for b,val2 in enumerate(inp):
					if len(val2)==1:
						tex = tex+val2[0]+"\n"
						print ("len(val2)",len(val2),val2)
						end = end+1
				fil = "cop.txt"
				f= open(fil,"w")
				print ("tex",tex)
				f.write(tex)
				f.close() 
				sw(fil,1)
				hod3(["ctrl","home",1,0])
				hod3(["shift","down",1,0])
				hod3(["ctrl","c",1,0])
				key2([["right",1,0,0],["left",1,0,0]])
				hit = hit+1
				if hit<end:
					alt(1,0)
				if hit==end:
					af4(1,1)
				fir = 1
		if len(val)==1:
			hod3(["ctrl","v",1,0])
			#if hit==end:
			#	continue
			if hit<end:
				alt(1,1)
				hod3(["shift","down",1,0])
				hod3(["ctrl","c",1,0])
				key2([["right",1,0,0],["left",1,0,0]])
				hit = hit+1
				if hit<end:
					alt(1,0)
				if hit==end:
					af4(1,1)
		if len(val)==2:
			val[0](val[1])
			#if val[0] == pgu2:


inp = []
run3(inp)