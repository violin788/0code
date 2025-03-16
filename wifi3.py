exec(open('util.py').read())
def wifi3(inp):
	
	# import module
	#import os
	 
	# scan available Wifi networks
	#os.system('cmd /c "netsh wlan show networks"')
	 
	# input Wifi name
	#name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
	#name_of_router = "CRRL" 

	# connect to the given wifi network
	#os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
	#print("reconnect of "+name_of_router+" commenceds") 
	#print("If you're not yet connected, try connecting to a previously connected SSID again!")

	#os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

	#"netsh interface set interface \"Wireless Network Connection\" admin=disabled"

	#netsh interface set interface "Wireless Network Connection" admin=disabled
	#netsh interface set interface "Wireless Network Connection" admin=enabled
	print ("now disabled..waiting 2 seconds!")
	os.system("netsh interface set interface \"Wireless Network Connection 2\" admin=disabled")
	time.sleep(2)
	os.system("netsh interface set interface \"Wireless Network Connection 2\" admin=enabled")
	print("now enabled!")
	print("wait 5 seconds..it will turn on! ")

inp = []
wifi3(inp)