exec(open('util.py').read())
def wifi(inp):



	os.system("ipconfig /release")
	print("")
	print("wifi turned off..waiting couple seconds to turn back on..")
	time.sleep(3)
	name_of_network = "CRRL"
	os.system(f'''cmd /c "netsh wlan connect name={name_of_network}"''')
	print("")
	print("ok, will prob take 5 or so seconds to connect...")
	

	#os.system("netsh interface set interface \"Wireless Network Connection 2\" admin=disabled")
	"""
	old one that was bad and actually turned off wifi card
	do not run this one

	print ("now disabled..waiting 2 seconds!")
	os.system("netsh interface set interface \"Wireless Network Connection 2\" admin=disabled")
	time.sleep(2)
	os.system("netsh interface set interface \"Wireless Network Connection 2\" admin=enabled")
	print("now enabled!")
	print("wait 5 seconds..it will turn on! ")
	"""		
	
	
inp = []
wifi(inp)