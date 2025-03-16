exec(open("util.py").read())
def nav(inp):
	#nav([])
	#nav([commands])
	#nav(["nav","nav2"])

	dri = dri_([])
	acc = acc_([])

	lib = []
	
	new = []
	nam = "pat"
	new = []
	new.append(nam)
	new.append([net,[0,["chr","r"]]])
	lib.append(new)
	
	new = []
	nam = "meb"
	new = []
	new.append(nam)
	lib.append(new)

	new = []
	nam = "tb"
	url = "https://docs.google.com/spreadsheets/d/1E9umtnbKku8wBp-7sB3btIkVcvsE6x4QOjHTl2SgrWk/edit?usp=drive_web&ouid=104465905925623639959"
	new = []
	new.append(nam)
	lib.append(new)

	new = []
	nam = "net"
	new = []
	new.append(nam)
	#new.append(spe)
	#new.append([but3,[["enter"],0,0]])
	new.append([net,[0,["chr","r"]]])
	lib.append(new)

	new = []
	nam = "ner"
	new = []
	new.append(nam)
	new.append([hod3,["win","right",1,1]])
	lib.append(new)

	new = []
	nam = "nel"
	new = []
	new.append(nam)
	new.append([hod3,["win","left",1,1]])
	lib.append(new)


	new = []
	nam = "nru"
	new = []
	new.append(nam)
	new.append([ne72,["ru"]])
	lib.append(new)

	new = []
	nam = "ctl"
	new = []
	new.append(nam)
	new.append([hod3,["ctrl","9",1,0]])
	lib.append(new)


	new = []
	nam = "nlu"
	new = []
	new.append(nam)
	#new.append(spe)
	#new.append([but3,[["enter"],0,0]])
	#new.append([ne72,[0,["chr","lu"]]])
	new.append([ne72,["lu"]])
	lib.append(new)

	new = []
	nam = "nrd"
	new = []
	new.append(nam)
	#new.append(spe)
	#new.append([but3,[["enter"],0,0]])
	#new.append([ne72,[0,["chr","rd"]]])
	new.append([ne72,["rd"]])
	
	lib.append(new)

	new = []
	nam = "nld"
	new = []
	new.append(nam)
	#new.append(spe)
	#new.append([but3,[["enter"],0,0]])
	#new.append([ne72,[0,["chr","ld"]]])
	new.append([ne72,["ld"]])	
	lib.append(new)


	#alr(["fir"])

	new = []
	nam = "che"
	new = []
	new.append(nam)
	#new.append(spe)
	#new.append([but3,[["enter"],0,0]])
	#new.append([ne72,[0,["chr","ld"]]])
	new.append([alr,["fir"]])	
	lib.append(new)


	new = []
	nam = "mlu"
	new = []
	new.append(nam)
	new.append([mot,["lu"]])
	lib.append(new)

	new = []
	nam = "mld"
	new = []
	new.append(nam)
	new.append([mot,["ld"]])	
	lib.append(new)

	new = []
	nam = "mru"
	new = []
	new.append(nam)
	new.append([mot,["ru"]])	
	lib.append(new)

	new = []
	nam = "mrd"
	new = []
	new.append(nam)
	new.append([mot,["rd"]])	
	lib.append(new)

	new = []
	nam = "mri"
	new = []
	new.append(nam)
	new.append([mot,["r"]])	
	lib.append(new)

	new = []
	nam = "mle"
	new = []
	new.append(nam)
	new.append([mot,["l"]])	
	lib.append(new)

	new = []
	nam = "csn"
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)

	nam = "med"
	url = "https://commonhelp.dss.virginia.gov/CASWeb/faces/loginCAS.xhtml?MODULE_NAME=CMB&SERVICE_PROVIDER=COMMON_HELP&LANGUAGE=EN"
	usn = "medicaid67"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)	
	run = []
	run.append([cf_ee5,["check bene",0,3]])
	run.append([hod3,["ctrl","t",1,1]])
	run.append(url)
	run.append([but3,[["enter"],1,3]])
	run.append([hod3,["ctrl","pageup",1,1]])
	run.append([hod3,["ctrl","f4",1,1]])
	run.append(usn)
	run.append([but3,[["enter"],0,3]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)


	#https://www.tinkercad.com/login
	new = []
	nam = "tin"
	new = []
	new.append(nam)
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)

	nam = "tra"
	url = "https://www.tradingview.com/chart/?symbol=AMEX%3ASPY"
	#usn = "media788788@gmail.com"
	#pas = "Medmed1!"
	"""
	ctrl f, continue
	esc, shift tab, enter
	wait 2 seconds
	tab, enter
	ctrl pageup 
	ctrl f4
	"""
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append([sle,[5]])
	run.append([cf_et3,["sign in with",1,0]])
	#run.append([but3,[["enter"],0,3]])
	run.append([key,[["tab",1,0,1]]])
	run.append([key,[["enter",1,0,2]]])
	run.append([key,[["tab",1,0,1]]])
	run.append([key,[["enter",1,0,1]]])
	run.append([hod3,["ctrl","pageup",1,1]])
	run.append([hod3,["ctrl","f4",1,1]])
	new.append(run)
	lib.append(new)	



	new = []
	nam = "wix"
	new = []
	new.append(nam)
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	


	new = []
	nam = "wor"
	new = []
	new.append(nam)
	new.append([wai,[]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append([cf_est,["password",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	new = []
	nam = "ren"
	#tech223@proton.me
	new = []
	new.append(nam)
	new.append([sle,[3]])
	#new.append([cf_etst,["log in"]])
	new.append([cf_ete,["log in"]])
	#cf_ete("log in"):
	new.append("usn")
	new.append([cf_etst,["password"]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)

	nam = "rel"
	url = "https://www.reddit.com/login/"
	usn = "savant78"
	pas = "savant77"

	#usn = "carpet222"
	#pas = "carcar123"
	#tech665533@gmail.com
	#usn = "water3322"
	#pas = "water123"
	#water3322
	#waterwater
	#acd561202@gmail.com
	new = []
	new.append(nam)	
	new.append(url)	
	run = []
	#run.append([cf,["apple"]])
	run.append([cf,["apple"]])
	run.append([key,[["esc",1,0,1]]])
	run.append([key,[["tab",2,0,1]]])
	#run.append(usn)
	run.append([cop3,[usn]])
	run.append([key,[["tab",1,0,1]]])
	run.append([cop3,[pas]])
	#run.append(pas)
	run.append([key,[["enter",1,0,1]]])
	new.append(run)	
	lib.append(new)	

	nam = "get"
	url = "https://gettr.com/landing"
	usn = ""
	pas = ""	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	#your soc
	run.append([cf,["your social"]])
	run.append([key,[["esc",1,0,1]]])
	run.append([key,[["tab",2,0,1]]])
	run.append([key,[["enter",1,0,1]]])
	new.append(run)
	lib.append(new)	



	new = []
	nam = "spo"
	new = []
	new.append(nam)
	new.append([sle,[3]])
	new.append([hod3,["ctrl","a",1,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	new.append([sle,[3]])
	new.append([cf_ee5,["web player",0,0]])
	lib.append(new)

	new = []
	nam = "fsk"
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)

	new = []
	nam = "lab"
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)

	new = []
	nam = "sk2"
	pas ="vioviovio1"
	new = []
	new.append(nam)
	new.append([sta,["skype.lnk"]])
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)

	new = []
	nam = "gom"
	new = []
	new.append(nam)
	new.append([sle,[1]])
	new.append([gom,[]])
	lib.append(new)

	"""
	usn = "199007305411"
	pas = "Celcel1!"
	inp = []
	inp.append([neu3,["https://online.swedbank.se/app/ib/logga-in",2,5]])
	#inp.append([init,["fof.txt"]])
	inp.append([usn])
	inp.append([cf2,["logga in",1]])
	inp.append([but3,[["enter"],0,0]])
	inp.append([cf_este3,["logga in",1,1]])


	fof3(inp)
"""


	new = []
	nam = "swe"
	new = []
	new.append(nam)
	new.append([sle,[1]])
	new.append("9007305411")
	new.append([cf3,["logga in",1]])
	new.append([but3,[["enter","esc"],1,0]])
	new.append([hod3,["shift","tab",1,0]])
	new.append([but3,[["enter"],0,0]])
	lib.append(new)
	
	new = []
	nam = "unh"
	amo = "1"
	ema = "violin78@protonmail.com"
	tel = "0731431617"
	idn = "199007305411"
	car = "5168 1531 3323 9073"
	dat = "04-24"
	cod = "818"

	new = []
	new.append(nam)
	#new.append([sle,[3]])
	new.append([sle,[6]])
	new.append([cf_est3,["valfritt",1,3]])
	new.append([but3,[["down","down","tab"],0,1]])
	new.append(amo)
	new.append([but3,[["tab"],0,0]])
	new.append(ema)
	new.append([but3,[["tab"],0,0]])
	new.append(tel)
	new.append([but3,[["tab"],0,0]])
	new.append(idn)
	new.append([but3,[["tab","tab","enter"],0,2]])
	new.append([cf_est3,["kortbe",1,1]])
	new.append([but3,[["down","tab","tab","enter"],0,10]])
	new.append([but3,[["tab"],0,0]])
	new.append(car)
	new.append([but3,[["tab"],0,0]])
	new.append(dat)
	new.append([but3,[["tab"],0,0]])
	new.append(cod)
	lib.append(new)
	
	new = []
	nam = "unh2"
	amo = "1"
	ema = "violin78@protonmail.com"
	tel = "0731431617"
	idn = "199007305411"
	car = "5168 1577 6580 9269"
	dat = "11-26"
	cod = "124"

	new = []
	new.append(nam)
	#new.append([sle,[3]])
	new.append([sle,[6]])
	new.append([cf_est3,["valfritt",1,3]])
	new.append([but3,[["down","down","tab"],0,1]])
	new.append(amo)
	new.append([but3,[["tab"],0,0]])
	new.append(ema)
	new.append([but3,[["tab"],0,0]])
	new.append(tel)
	new.append([but3,[["tab"],0,0]])
	new.append(idn)
	new.append([but3,[["tab","tab","enter"],0,2]])
	new.append([cf_est3,["kortbe",1,1]])
	new.append([but3,[["down","tab","tab","enter"],0,10]])
	new.append([but3,[["tab"],0,0]])
	new.append(car)
	new.append([but3,[["tab"],0,0]])
	new.append(dat)
	new.append([but3,[["tab"],0,0]])
	new.append(cod)
	lib.append(new)

	nam = "afe"
	new = []
	new.append(nam)
	new.append([sle,[3]])
	new.append([cf_etm3,["route",1]])
	new.append([sle,[2]])
	new.append(["Rostock - Trelleborg"])
	new.append([sle,[2]])
	new.append([but3,[["down","enter","enter"],1,0]])
	lib.append(new)
	
	nam = "cra"
	new = []
	new.append(nam)
	new.append([sle,[2]])
	#new.append([cfb,["email",[["esc",1,0,1],["tab",1,0,1]]]])
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	
	
	"""


	url = "https://www.paypal.com/us/signin"
	usn = "gocubs7@protonmail.com"
	pas = "Vvbd63Vvbd63"
	#inp.append([cf_et4(text)])	
	inp = []
	inp.append([neu3,[url,2,5]])
	inp.append([but3,[["tab"],0,1]])
	#inp.append([cf_et5,["account",1,1]])
	inp.append([usn])
	inp.append([but3,[["enter"],0,4]])
	inp.append([pas])
	inp.append([but3,[["enter"],0,0]])
	fof3(inp)


	
	url = "https://mychart.mwhc.com/mychart/Billing/Details?ID=WP-24BZ0G8iQup-2B0YpR6dV6umeQ-3D-3D-24HyCPRBVi9Tsd0DWVi57-2Bv0ZSpX9HMaYHmhQB7Yh07WI-3D&Context=WP-24kaa7uki37RKmJYXx9C3DdQ-3D-3D-24w-2B8Fh5dBnlLOcSy9SzR8Eu1gObDNVjvEi30vpI14S7s-3D"	
	usn = "mwhos"
	pas = "mwhos123"



	usn = "cello34"
	pas = "Celcel1!"
	inp = []
	inp.append([neu3,["https://myvhc.virginiahospitalcenter.com/MyChartPRD/Authentication/Login?",2,5]])


exec(open('util.py').read())
def tapl():
	url = "https://www.flytap.com/en-us/login"
	usn = "violin78@protonmail.com"
	pas = "Viovio1!"
	#inp.append([cf_et4(text)])	
	inp = []
	inp.append([neu3,[url,2,5]])
	inp.append([cf_et5,["account",1,1]])
	inp.append([usn])
	inp.append([but3,[["tab"],0,0]])
	inp.append([pas])
	inp.append([but3,[["enter"],0,0]])
	fof3(inp)





inp = []
tapl(inp)


	"""





	new = []
	nam = "mwh"
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([sle,[1]])
	new.append([but3,[["enter"],0,0]])
	lib.append(new)
	
	nam = "atl"
	url = "https://www.atlanticunionbank.com/?matchtype=p&network=g&device=c&adposition&keyword=atlantic+union+bank&gclid=CjwKCAjwoNuGBhA8EiwAFxomA-IVTR0LN_auLWy4skF8k6Yh4YotKwkTMlb1TdqlCJZsMVSXLcbPrhoCI0cQAvD_BwE"
	usn = "atlatl"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)	
	run = []
	run.append([cf_ee5,["login",0,2]])
	run.append([but3,[["tab","tab"],0,1]])
	run.append(usn)
	run.append([but3,[["tab"],0,0]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)

	nam = "atl4"
	url = "https://www.atlanticunionbanksecure.com/dbank/live/app/login/consumer"
	usn = "atlatl"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)	
	run = []
	run.append([cf_ee5,["login",0,2]])
	run.append([but3,[["tab","tab"],0,1]])
	run.append(usn)
	run.append([but3,[["tab"],0,0]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)

	
	def atl3(inp):
		hod3(["ctrl","pageup",1,1])
		sle([5])
		cf_este3(["email me",1,2])
		hod3(["ctrl","pagedown",1,1])


	nam = "atl2"
	new = []
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	#new.append([but3,[["enter"],0,0]])
	#new.append([atl3,[]])
	new.append([hod3,["ctrl","pageup",1,1]])
	new.append([sle,[5]])
	new.append([cf_este3,["email me",1,2]])
	new.append([hod3,["ctrl","pagedown",1,1]])
	lib.append(new)	
	
	nam = "ant"
	url = "https://member.anthem.com/public/login"
	usn = "violin78"
	pas = "Medmed1!"
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([sle,[2]])
	run.append([key,[["tab",2,0,1]]])
	run.append(usn)
	run.append([key,[["tab",1,0,1]]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)

	nam = "sky"
	url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1605518694&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3A%2F%2Flw.skype.com%2Flogin%2Foauth%2Fproxy%3Fclient_id%3D360605%26redirect_uri%3Dhttps%253A%252F%252Fsecure.skype.com%252Fportal%252Flogin%253Freturn_url%253Dhttps%25253A%25252F%25252Fsecure.skype.com%25252Fportal%25252Foverview%26response_type%3Dpostgrant%26state%3Dceafc3abe521398a95d4997c&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFlight67"
	usn = "violin78@mail.com"
	pas = "vioviovio1"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append(usn)
	run.append([but3,[["enter"],0,3]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)	
	lib.append(new)	

	new = []
	nam = "sky2"
	#url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1651348909&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3A%2F%2Flw.skype.com%2Flogin%2Foauth%2Fproxy%3Fclient_id%3D572381%26redirect_uri%3Dhttps%253A%252F%252Fweb.skype.com%252FAuth%252FPostHandler%26state%3Dbd4d509f-29bd-4470-8942-0f633699bce0&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFlight67"
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)


	nam = "go1"
	new = []
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["enter"],0,3]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	nam = "dri"
	url = "https://accounts.google.com/v3/signin/identifier?continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ifkv=AVQVeywOm-k8hP4krxDG65AtJJsfoDk2BqIyZioBsuIsXN5r8-Ury6a5TzRkYLCx6aaIRiizNKhATg&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1845268536%3A1698099420719416&theme=glif"
	#usn1 = "media78878"
	#usn2 = "8"
	#pas = "Medmed1!"
	#usn1 = "library505050"
	#usn2 = "0"
	#pas = "Liblib1!"
	usn = "media788788@gmail.com"
	pas = "Medmed1!"

	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([sle,[4]])
	run.append([cop3,[usn]])
	run.append([but3,[["enter"],0,5]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	

	nam = "voi"
	url = ""
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([voi2,[]])
	new.append(run)
	lib.append(new)	


	nam = "pro"
	url = "https://mail.protonmail.com/login"
	usn = "violin78"
	pas = "viovio"	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([sle,[2]])
	#run.append([cf_et3,["email",1,0]])
	run.append(usn)
	run.append([but3,[["tab"],0,0]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	

	nam = "low"
	url = "https://www.lowes.com/u/login/oauth2/authorize?redirect_uri=https%3A%2F%2Fwww.lowes.com%2Fu%2Flogin%2Foauth2%2Fpostauthorize&scope=general-digital-access&client_id=loweswebclient&state=VjNJdkhSS1ZWSldnSmplYmNvakJkd0JTT0xzcGpNM0Nrb0wzNGZveUdTTGRTb1hDYUJhU0Z6RDVES3l0ZnZ0Sg%3D%3D&code_challenge=kfnk1cdJSBlp0L_S75hsh-YrDZE5epbwE1JVh3PbeoY&code_challenge_method=S256&redirect="
	usn = "media788788@gmail.com"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append([cf_et3,["lowe",1,0]])
	run.append(usn)
	run.append([but3,[["tab"],0,1]])
	run.append(pas)
	run.append([but3,[["enter"],0,5]])
	run.append([hod3,["alt","d",1,1]])
	ano = "https://www.lowes.com/u/login/oauth2/postauthorize?code=BidJzcKl7NvZfiIDNJsnR3qtX9g&state=bE1NNENXazBsbXoxR2pnR1RVeHBjSjBKUmk1MWZDdThKVm11OGJBYXYwejdKQXlDZTlIbWNaQkdzeEhTZ0hMbA%3D%3D&client_id=loweswebclient&tokenId=lB_ZhGugFm9KXaVes27chNiY6bs.*AAJTSQACMDgAAlNLABxDN2ZIV2E5YmR1YkxZM3ZCaU5waXFmVDRlMGM9AAR0eXBlAANDVFMAAlMxAAIxMg..*"
	run.append([wri4,[3,"lowes.com"]])
	run.append([but3,[["enter"],0,5]])
	run.append([cf_etste3,["sign in",0,5]])
	run.append([cf_etste3,["sign in",2,0]])
	new.append(run)
	lib.append(new)	


	"""
	https://www.homedepot.com/auth/view/signin
	tab 3x
	media788788@gmail.com
	"""


	nam = "hom"
	#url = "https://www.lowes.com/u/login/oauth2/authorize?redirect_uri=https%3A%2F%2Fwww.lowes.com%2Fu%2Flogin%2Foauth2%2Fpostauthorize&scope=general-digital-access&client_id=loweswebclient&state=VjNJdkhSS1ZWSldnSmplYmNvakJkd0JTT0xzcGpNM0Nrb0wzNGZveUdTTGRTb1hDYUJhU0Z6RDVES3l0ZnZ0Sg%3D%3D&code_challenge=kfnk1cdJSBlp0L_S75hsh-YrDZE5epbwE1JVh3PbeoY&code_challenge_method=S256&redirect="
	url = "https://www.homedepot.com/auth/view/signin"
	usn = "media788788@gmail.com"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append([sle,[3]])
	run.append([key,[["tab",3,0,1]]])
	run.append([but3,[["enter"],0,5]])
	new.append(run)
	lib.append(new)	


	nam = "prn"
	new = []
	new = []
	new.append(nam)
	new.append([cf_et3,["email",1,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	nam = "prv"
	new = []
	new = []
	new.append(nam)
	new.append([cf_et3,["email",1,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	nam = "prc"
	new = []
	new = []
	new.append(nam)
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	nam = "prc2"
	new = []
	new = []
	new.append(nam)
	new.append([sle,[3]])
	
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	nam = "fac"
	url = "https://www.facebook.com"
	usn = "violin78@protonmail.com"
	pas = "Viovio1!"	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	#run.append([cf_et3,["email",1,0]])
	run.append([sle,[2]])
	run.append(usn)
	run.append([but3,[["tab"],0,1]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)

	nam = "iex"
	new = []
	new = []
	new.append(nam)
	new.append("usn")
	new.append([key,[["tab",2,0,0]]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	


	nam = "tar"
	new = []
	new = []
	new.append(nam)
	new.append([sle,[3]])
	new.append([but3,[["tab","tab","tab","tab"],0,0]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	


	nam = "quo"
	new = []
	new = []
	new.append(nam)
	new.append("usn")
	#new.append([cf_et5,[usn,2,2]])
	#new.append([cf_et5,[usn,1,0]])
	new.append([cf_et5,["usn",1,1]])	
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	#https://twitter.com/notifications
	nam = "twi"
	#url = "https://twitter.com/i/flow/login"
	url = "https://twitter.com/notifications"
	#usn = "media788788@gmail.com"
	#usn = "oversight2836"
	usn = "oversight333"
	pas = "Oveove1!"
	new = []
	new.append(nam)	
	new.append(url)	
	run = []
	
	run.append([cf,["to x"]])
	run.append([key,[["esc",1,0,1]]])
	run.append([key,[["tab",3,0,1]]])
	run.append(usn)
	run.append([key,[["enter",1,0,2]]])
	run.append(pas)
	run.append([key,[["enter",1,0,1]]])
	new.append(run)	
	lib.append(new)		

	nam = "nel"
	new = []
	new = []
	new.append(nam)
	#new.append([cf_ete2,["google",2]])
	new.append([cf_ete2,["continue",2]])
	new.append([key,[["tab",1,0,1],["enter",1,0,1]]])
	lib.append(new)		
	nam = "ner"
	new = []
	new = []
	new.append(nam)
	#new.append([cf_ete2,["google",2]])
	new.append([cf_ete2,["continue",2]])
	new.append([key,[["tab",1,0,1],["enter",1,0,1]]])
	lib.append(new)		

	nam = "caf"
	url = "https://docs.google.com/spreadsheets/d/1Vud_RNLLOEAMeyHwLF0oY24Jp_s_8FqYmF8DMnyuvqA/edit#gid=0"
	#url = "https://docs.google.com/spreadsheets/d/112faALhmpQg_kIDjJYaOdDHuYZlrHL1e/edit?pli=1#gid=1924957846"
	usn = ""
	pas = ""	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([hod3,["ctrl","r",1,0]])
	new.append(run)
	lib.append(new)	

	nam = "kee"
	url = "https://keep.google.com/"
	usn = ""
	pas = ""	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([hod3,["ctrl","r",1,0]])
	new.append(run)
	lib.append(new)		

	nam = "gma"
	#url = "https://mail.google.com/mail/u/0/#inbox"
	url = "https://mail.google.com/mail/u/0/"
	usn = ""
	pas = ""	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([hod3,["ctrl","r",1,0]])
	new.append(run)
	lib.append(new)	

	nam = "red"
	url = "https://docs.google.com/spreadsheets/d/1qrySuja-rx_LoHcXIoLAidd1C92hqyeouNv2O7iWnDs/edit#gid=0"
	#url = "https://docs.google.com/spreadsheets/d/16cDVvBNoXtbcqKv3ZyXqFTBW-PPGCGOz/edit#gid=2118827479"
	usn = ""
	pas = ""	
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([hod3,["ctrl","r",1,0]])
	new.append(run)
	lib.append(new)	

	nam = "ins"
	new = []
	new = []
	new.append(nam)
	new.append([cf_et5,["phone",1,0]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	

	nam = "inc"
	new = []
	new = []
	new.append(nam)
	#new.append([cf_ee5,["log in",1,1]])
	#cf_etste3(["log in",0,2])
	new.append([sle,[3]])
	new.append([cf_etste3,["log in"]])
	new.append([sle,[2]])
	new.append([key,[["tab",2,0,1]]])
	
	#key([["esc",1,0,0],["tab",2,0,0],["space",2,0,0]])
	
	#cf_etste3(["log in"])
	
	#new.append([but3,[["tab","tab"],0,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,0]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)	



	"""
	nam = "pla"
	new = []
	new = []
	new.append(nam)
	new.append([sle,[3]])
	new.append([key,[["tab",3,0,1]]])
	new.append("usn")
	new.append([but3,[["tab"],0,1]])
	new.append("pas")
	new.append([but3,[["enter"],0,1]])
	lib.append(new)
	"""

	nam = "pla"
	url = "https://planner5d.com/"
	usn = "violin78@protonmail.com"
	pas = "viovio"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#run.append([cf_et3,["email",1,0]])
	run.append(usn)
	run.append([but3,[["enter"],0,3]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	



	nam = "har"
	url = "https://order.hardees.com/account/login"
	usn = "media788788@gmail.com"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append([cf,["email"]])
	run.append([key,[["esc",1,0,1]]])
	run.append([key,[["tab",1,0,1]]])
	run.append(usn)
	run.append([but3,[["tab"],0,1]])
	run.append(pas)
	run.append([but3,[["tab"],2,1]])
	run.append([but3,[["space"],1,1]])
	run.append([but3,[["tab"],1,1]])
	run.append([but3,[["enter"],1,1]])
		

	#run.append([but3,[["enter"],0,1]])
	

	#run.append([cf_este3,["google",0,5]])
	#run.append([cf_este3,["start order",0,0]])
	#run.append(usn)
	#run.append([but3,[["tab"],0,1]])
	#run.append(pas)
	#run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	


	nam = "git"
	url = "https://github.com/login"
	usn = "media788788@gmail.com"
	pas = "media788788"
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append(usn)
	run.append([but3,[["tab"],0,1]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)

	nam = "aws"
	new = []
	new = []
	new.append(nam)
	new.append([sle,[3]])
	#new.append([cf_et5,["account",1,1]])
	new.append("usn")
	new.append([but3,[["tab"],0,2]])
	new.append("pas")
	new.append([but3,[["enter"],0,0]])
	lib.append(new)



	nam = "cvs"
	
	new = []
	new = []
	new.append(nam)
	new.append([sle,[3]])
	new.append([cf_et5,["address",1,1]])
	new.append("book56@protonmail.com")
	new.append([but3,[["enter"],0,2]])
	new.append([but3,[["tab"],0,1]])
	new.append("Booboo1!")
	new.append([but3,[["enter"],0,2]])
	lib.append(new)

	nam = "nas"
	new = []
	new.append(nam)
	new.append([cf_et5,["email",1,1]])
	new.append("usn")
	new.append([key,[["tab",1,0,1],["enter",1,0,1]]])
	new.append("pas")
	new.append([key,[["tab",1,0,1],["enter",1,0,1]]])
	lib.append(new)


	nam = "ama"
	url = "https://www.amazon.com/gp/css/order-history?ref_=nav_AccountFlyout_orders"
	usn = "media788788@gmail.com"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#run.append([cf_et3,["email",1,0]])
	run.append(usn)
	run.append([but3,[["enter"],0,3]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	

	nam = "ebay"
	url = "https://www.ebay.com/signin/"
	usn = "media788788@gmail.com"
	pas = "Medmed1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append([cf_et3,["email",1,0]])
	run.append(usn)
	run.append([but3,[["enter"],0,3]])
	run.append([but3,[["tab"],0,1]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	

	nam = "wea1"
	#url = "https://mail.google.com/mail/u/0/#inbox"
	url = "https://weather.com/weather/radar/interactive/l/Fredericksburg+VA?canonicalCityId=08a051206dd97b486cb0128338def846c6fcec0d29766b8f97755b41321b1215"
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([hod3,["ctrl","r",1,0]])
	new.append(run)
	lib.append(new)	

	nam = "wea2"
	#url = "https://mail.google.com/mail/u/0/#inbox"
	url = "https://www.google.com/search?client=browser-b-1-d&q=weather"
	new = []
	new.append(nam)
	new.append(url)
	run = []
	run.append([hod3,["ctrl","r",1,0]])
	new.append(run)
	lib.append(new)	

	nam = "dmv"
	url = "https://transactions.dmv.virginia.gov/apps/webtrans/pin_maint/pin_logon.aspx"
	usn = "212331006"
	pas = "Viovioviovio1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#run.append([cf_et3,["email",1,0]])
	run.append([cf,["hyphen"]])
	run.append([key,[["esc",1,0,1]]])
	run.append([key,[["tab",1,0,1]]])
	run.append(usn)
	run.append([key,[["tab",1,0,1]]])
	run.append("07")
	run.append([key,[["tab",1,0,1]]])
	run.append("30")
	run.append([key,[["tab",2,0,1]]])
	run.append("90")
	run.append([but3,[["enter"],0,0]])
	run.append([sle,[2]])
	run.append([cf,["password"]])
	run.append([key,[["esc",1,0,1]]])
	run.append([key,[["tab",1,0,1]]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	



	nam = "lin"
	url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
	usn = "violin78@protonmail.com"
	pas = "Viovio1!"	
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#run.append([cf_et3,["email",1,0]])
	run.append(usn)
	run.append([but3,[["tab"],0,1]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	

	#32 bit
	#browser_location = "browser-32bit.lnk"
	#browser_location = "browser-32bit.lnk" 
	#browser_location = "firefox-32bit.lnk"
	browser_location = "opera-32bit.lnk"
	#opera_location
	#browser_location


	nam = "new_left"
	url = ""
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#aut3_loc = dri+"\\Users\\"+acc+"\\util\\aut3.html"
	browser =browser_location
	#aut3_loc="browser.lnk"
	urls = []
	#run.append([opa,["aut3.html",urls]])
	run.append([start_file,[browser,2]])
	run.append([start_file,["aut3.html",2]])
	run.append([hod3,["win","left",1,2]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([open_button,[browser]])
	run.append([sle,[2]])
	new.append(run)
	lib.append(new)	

	nam = "new_right"
	url = ""
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#aut3_loc = dri+"\\Users\\"+acc+"\\util\\aut3.html"
	browser =browser_location
	#aut3_loc="browser.lnk"
	urls = []
	#run.append([opa,["aut3.html",urls]])
	run.append([start_file,[browser,2]])
	run.append([start_file,["aut3.html",2]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([open_button,[browser]])
	run.append([sle,[2]])
	run.append([hod3,["win","right",1,1]])
	new.append(run)
	lib.append(new)	

	nam = "new"
	url = ""
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	browser =browser_location
	urls = []
	#run.append([opa,["aut3.html",urls]])
	run.append([start_file,[browser,2]])
	run.append([start_file,["aut3.html",2]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([open_button,[browser]])
	new.append(run)
	lib.append(new)	

	nam = "alt"
	url = ""
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	run.append([hod3,["alt","tab",1,1]])
	run.append([start_file,["aut3.html",2]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([open_button,[browser]])

	#run.append([hod3,["alt","tab",1,1]])
	#run.append([open_button,[browser]])
	new.append(run)
	lib.append(new)	

	nam = "nav2"
	url = ""
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#aut3_loc = dri+"\\Users\\"+acc+"\\util\\aut3.html"
	browser =browser_location
	#aut3_loc="browser.lnk"
	run.append([start_file,[browser,2]])
	run.append([start_file,["aut3.html",2]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([hod3,["alt","tab",1,1]])
	run.append([open_button,[browser]])
	new.append(run)
	lib.append(new)	

	
	nam = "ed1"
	#url = "file:///A:/Users/-/0c/webf.html"
	new = []
	new = []
	new.append(nam)
	new.append([cf_ee5,["login",0,2]])
	lib.append(new)

	nam = "ed2"
	#new = []
	new = []
	new.append(nam)
	new.append([hod3,["ctrl","r",1,2]])
	lib.append(new)


	nam = "wal"
	url = "https://www.walmart.com/account/login?vid=oaoh&tid=0&returnUrl=%2F"
	usn = "violin78@protonmail.com"
	pas = "Viovio1!"
	new = []
	new.append(nam)	
	new.append(url)
	run = []
	#run.append([cf_et3,["email",1,0]])
	run.append(usn)
	run.append([but3,[["enter"],0,3]])
	run.append(pas)
	run.append([but3,[["enter"],0,0]])
	new.append(run)
	lib.append(new)	
	return lib	

processes = nav([])

#https://www.walmart.com/account/login?vid=oaoh&tid=0&returnUrl=%2F
if __name__=="__main__":
	lib = processes
	#print("bark")

	usn = "---"
	pas = "---"
	url = "---"

	wea = []
	wea.append("wea1")
	wea.append("wea2")

	default = []
	#default.append("new")
	default.append("new_left")
	default.append("dri")
	default.append("red")
	#default.append("caf")
	default.append("kee")
	default.append("gma")
	default.append("pro")
	default.append("fac")
	default.append("rel")
	default.append("twi")
	#default.append("get")
	default.append("voi")
	#pri(ope)



	#inputs = inp
	#if len(inputs)>0:
	#	run = inputs
	#if len(inputs)==0:
	run = whi("to run?")
	#run = ["twi","ama"]
	#run = ["ope"]
	if "wea" in run:
		run.append("wea1")
		run.append("wea2")
	mas = []
	ope2 = []
	#if "nav" in run or "nav2" in run:
	#gen urls
	che = []
	che.append(run)
	che = che[0]
	urls = []
	get_urls = run
	#general url file
	if "nav" in run or "nav2" in run:
	#if "nav" in run:
		get_urls = default
	for a,val in enumerate(get_urls):
		for b,valb in enumerate(lib):
			nam1 = val
			nam2 = valb[0]
			if nam1==nam2:
				print(nam1,nam2)
				url = valb[1]
				if len(url)>0:
					urls.append(url)
	if "firefox" in browser or "chrome" in browser:
		urls = urls[::-1]
	if "Firefox" in browser or "Chrome" in browser:
		urls = urls[::-1]
	pri(urls)
	#sye()
	#if "opera" in browser or "Opera" in browser:
	opa(["aut3.html",urls])	
	#sye()
	print(default)
	pri(run)
	run2 = []
	for a,val in enumerate(run):
		if val=="nav":
			for b,valb in enumerate(default):
				run2.append(valb)
			continue
		if val=="nav2":
			#run2.append("new")
			run2.append("new_right")
			continue
		if val!="nav" and val!="nav2":
			run2.append(val)
	run = run2
	if "new" not in run:
		if "new_left" not in run:
			if "new_right" not in run:
				run = ["alt"]+run
	pri(run)
	#sye()
	for a,val in enumerate(run):
		for b,valb in enumerate(lib):
			nam1 = val
			nam2 = valb[0]
			if nam1==nam2:
				if nam1=="new":
					mas.append([opa,["aut3.html",urls]])
				print(nam1)
				url = valb[1]
				wtd = valb[2]
				ope2.append(url)
				for c,valc in enumerate(wtd):
					mas.append(valc)
				#pri(wtd)
				if val!="new":
					if val!="new_right":
						if val!="new_left":
							if a<len(run)-2:
								mas.append([hod3,["ctrl","pagedown",1,0]])
	pri(mas)
	#sye()
	
	#print(che)
	for a,val in enumerate(mas):
		if type(val)==str:
			mas[a]=[wri3,[val,1]]
	for a,val in enumerate(mas):
		print(val)
		val[0](val[1])		
inp = []
nav(inp)