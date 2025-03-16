exec(open('util.py').read())
def iex(inp):
	#iex1 = pk_b9423430ffab4eba94643e692f8f3421
	#iex2 = sk_5b0fffcc5b24496382bca4e076f4a0bf
	#secret
	
	"""
	import pyEX as p
	c = p.Client(api_token='YOUR_API_TOKEN', version='stable')
	"""

	import pandas as pd
	import pyEX as p

	#tickers = ['AAPL', 'FB', 'AMZN', 'GOOGL', 'NFLX']
	#c = p.Client(api_token='YOUR_TOKEN_HERE', version='sandbox')
	#c = p.Client(api_token='pk_b9423430ffab4eba94643e692f8f3421', version='sandbox')
	tickers = ['AAPL']
	c = p.Client(api_token='pk_b9423430ffab4eba94643e692f8f3421')
	#res = pd.DataFrame(c.batchDF(symbols=tickers, fields='chart', last=365, range_='1y')['chart'])
	res = pd.DataFrame(c.batchDF(symbols=tickers, fields='chart', last=10))
	print (res)


inp = []
iex(inp)

"""
https://sandbox.iexapis.com/stable/stock/market/batch?token=YOUR_TOKEN&range=5d&types=chart,intraday-prices&symbols=FB,AAPL,AMZN,NFLX,GOOG&chartIEXOnly=True

https://sandbox.iexapis.com/stable/stock/market/batch?token=YOUR_TOKEN&range=1d&types=chart&symbols=FB,AAPL,AMZN,NFLX,GOOG

https://cloud.iexapis.com/stable/stock/market/batch?token=pk_b9423430ffab4eba94643e692f8f3421&range=5d&types=chart&symbols=FB,AAPL,AMZN,NFLX,GOOG

TSLA,JNJ,RHHBY,PG,NSRGY,BAC,DHR,ABT,LRLCY,ASML,VZ,SCHW,PM,HESAY,BHP,UNP,ELV,IBM,T,AXP,NFLX,BX,GS,RIO,MMC,PLD,ISRG,ESLOY,WMMVY

10-03
https://cloud.iexapis.com/stable/stock/market/batch?token=pk_b9423430ffab4eba94643e692f8f3421&range=5d&types=chart&symbols=STZb,STZ,SVNDY,MKCv,MKC,TSCDY,CAG,AONNY,LW,RPM,LEVI,AYI,HELE,SAND,NG,NFJ,CSVI,BTT,VLGEA,TMQ,SGH,SAR,RGP,RELL,QK,PMF,PKE,PCQ,NRIX,NIE,MYI,MUI,LNDC,IDT,FEEXF,CSCW,BYRN,BTA,ARTW,ANGO,AEHR,ACCD

10-10
https://cloud.iexapis.com/stable/stock/market/batch?token=pk_b9423430ffab4eba94643e692f8f3421&range=5d&types=chart&symbols=UNH,TSM,JPM,LVMUY,PEP,WFC,MS,C,BLK,INFY,PGR,PNC,USB,FRCOY,FSUMF,WBA,WIT,FAST,FRC,DAL,LGGNY,DPZ,CRRFY,ASXFY,CHYHY,RGLD,CMC,RYKKY,WAFD

10-17
https://cloud.iexapis.com/stable/stock/market/batch?token=pk_b9423430ffab4eba94643e692f8f3421&range=5d&types=chart&symbols=TSLA,JNJ,RHHBY,PG,NSRGY,BAC,DHR,ABT,LRLCY,ASML,VZ,SCHW,PM,HESAY,BHP,UNP,ELV,IBM,T,AXP,NFLX,BX,GS,RIO,MMC,PLD,ISRG,ESLOY,WMMVY

10-24
https://cloud.iexapis.com/stable/stock/market/batch?token=pk_b9423430ffab4eba94643e692f8f3421&range=5d&types=chart&symbols=XOM,V,META,CVX,ABBV,KO,MRK,IDCBY,TMO,SHEL,MCD,NVS,BMY,CICHY,NEE,UPS,TXN,LIN,UL,CMCSA,PTR,TTE,RTX,HON,EQNR,PNGAY,INTC,BYDDY,LMT,HSBC,LFC,SAP,SPGI,CAT,BYDDF,ADP,BUD,AMT,GILD,BTI,MO,SONY

secret token
sk_5b0fffcc5b24496382bca4e076f4a0bf

https://cloud.iexapis.com/stable/stock/market/batch?token=sk_5b0fffcc5b24496382bca4e076f4a0bf&range=5d&types=chart&symbols=NKE,MU,PAYX,CTAS,FERG,KMX,MTN,JBL,SNX,JEF,CNXC,THO,DAVA,WOR,UNFI,NEOG,EXG,CBRL,CALM,BB,UEC,PRGS,NAPA,MLKN,MFGP,EVV,ETY,EPAC,ZKIN,WINR,VZLA,VRAR,VIAO,VALV,UPXI

"""

#https://cloud.iexapis.com/stable/stock/market/batch?token=____&range=5d&types=chart&symbols=NKE,MU,PAYX,CTAS,FERG,KMX,MTN,JBL,SNX,JEF,CNXC,THO,DAVA,WOR,UNFI,NEOG,EXG,CBRL,CALM,BB,UEC,PRGS,NAPA,MLKN,MFGP,EVV,ETY,EPAC,ZKIN,WINR,VZLA,VRAR,VIAO,VALV,UPXI
