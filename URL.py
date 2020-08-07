import pyshorteners
import time
while True:
	try:

		url = input("URL (type exit to exit) :  ")
		if url == "exit":
			print("Goodbye ! ")
			break
			
		else:
			s = pyshorteners.Shortener().tinyurl.short(url)
			time.sleep(3)
			print("Shortened : ", s)
		
	
	except:

		print("Something wrong happened")
		time.sleep(1)
		print("Contact 2003emirkanesme@gmail.com")
		time.sleep(1)