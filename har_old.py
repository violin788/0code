exec(open('util.py').read())
def har(inp):
	inp = inp
	x = 3
	ray=  []
	sta = 0
	ray.append([hod3,["alt","tab",1,1]])
	ray.append([cf_este,"recents"])
	ray.append([sle,[x]])
	ray.append([cf_este,"start order"])
	ray.append([sle,[x]])
	ray.append([cf_este,"sides"])
	ray.append([sle,[x]])
	ray.append([cf_ete,"jala"])
	ray.append([sle,[x]])
	ray.append([cf_este,"add to"])
	ray.append([sle,[x]])
	#ray.append([alt2,[1,1]])
	ray.append([hod3,["alt","d",1,1]])
	
	ray.append([key3,[["tab",6,1,0],["enter",1,0,5]]])
	#ray.append([key3,[["enter",1,0,5]]])
	

	"""
	ray.append([alt2,[1,1]])
	ray.append([alt2,[1,1]])
	ray.append([num2,["https://order.hardees.com/order/my-bag",5]])
	#https://order.hardees.com/order/my-bag
	"""
	ray.append([wri3,["checkout",1]])
	#ray.append([cf_este,"check out"])
	ray.append([sle,[x]])
	ray.append([cf_este,"place order"])

	for a in range(sta,len(ray)):
		val = ray[a]
		val[0](val[1])

#def poke_lisa():
inp = []
har(inp)