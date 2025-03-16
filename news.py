exec(open('util.py').read())
def news(inp):
	
	import sched
	import time

	# Create a scheduler object
	scheduler = sched.scheduler(time.time, time.sleep)

	# Define the function you want to execute
	def my_process():
		#https://rumble.com/v3by09g-warroom-live.html
		subprocess_open([5,"https://rumble.com/v3by09g-warroom-live.html","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
	    #print("Executing my_process at", time.time())

	# Schedule your process to run at a specific time (in this example, after 10 minutes)
	scheduler.enter(600, 1, my_process, ())

	# Run the scheduler
	scheduler.run()
	
	
inp = []
news(inp)