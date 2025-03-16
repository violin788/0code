exec(open('util.py').read())
def fln_codes_do_not_delete(ray):

	eur = []
	eur.append(["arn","/m/06mxs"])
	eur.append(["got","GOT"])
	eur.append(["osl","/m/05l64"])
	eur.append(["cph","CPH"])
	eur.append(["ber","BER"])
	eur.append(["fra","/m/02z0j"])
	eur.append(["par","/m/05qtj"])
	eur.append(["lon","/m/04jpl"])

	con = rea4(["tes3",'txt'])

	for a,val in enumerate(eur):
		print (val[0])
		con = con.replace(val[0],"ray.append([\""+val[0]+"\",")
		con = con.replace(",\n,",",")



	print (con)
	sys.exit()

	alt(1,1)
	wri("arn",1)

	ray = ray
	"""inp = []
fln_codes_do_not_delete(inp)