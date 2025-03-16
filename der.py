exec(open('util.py').read())
def der(inp):

	inputs = []
	inputs.append("stock symbol")
	inputs.append("price")
	inputs.append("expiration day")
	inputs.append("expiration month")
	inputs.append("expiration year (2 digits)")
	inputs.append("c for call, p for put")
	inputs = whi4([inputs])
	for a,val in enumerate(inputs):
		inputs[a] = val.upper()
	pri(inputs)
	symbol = inputs[0]
	price = inputs[1]
	expiration_day = inputs[2]
	expiration_month = inputs[3]
	expiration_year = inputs[4]
	call_or_put = inputs[5]
	if len(expiration_day)==1:
		expiration_day = "0"+expiration_day
	if len(expiration_month)==1:
		expiration_month = "0"+expiration_month
	url_finviz_1 = "https://finviz.com/quote.ashx?t="
	url_finviz_2 = "&ty=oc&ov=chain_strike&s="
	url_finviz = url_finviz_1+symbol+url_finviz_2+price
	url_yahoo_1 = "https://finance.yahoo.com/chart/"
	#url_yahoo_2 = "&ty=oc&ov=chain_strike&s="
	yahoo_price = str(float(price))
	#SPY240308C00515500
	yahoo_price = yahoo_price.replace(".","")+"00"
	for a in range(0,8-len(yahoo_price)):
		yahoo_price = "0"+yahoo_price
	print(yahoo_price)
	#sye()
	url_yahoo = url_yahoo_1+symbol+expiration_year+expiration_month+expiration_day
	url_yahoo = url_yahoo+call_or_put+yahoo_price
	urls = [url_finviz,url_yahoo]
	#opa3(["aut3",urls])
	opa3(["deriv",urls])
	#num6([url,2,1])
	#num5([url,2])
	#https://finviz.com/quote.ashx?t=MSFT&ty=oc&ov=chain_strike&s=402.50
	#https://finviz.com/quote.ashx?t=MSFT&ty=oc&e=2024-03-08
	
	
inp = []
der(inp)