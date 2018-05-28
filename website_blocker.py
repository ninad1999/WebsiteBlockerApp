import time
from datetime import datetime as dt

host_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = ["facebook.com", "wwww.facebook.com", "www.youtube.com", "youtube.com", "www.instagram.com", "instagram.com", "netflix.com", "www.netflix.com"]

while True:

	if ((dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 12, 30)) or
	  (dt(dt.now().year, dt.now().month, dt.now().day, 14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21))) :
		print("WORKING HOURS")
		with open(host_path, 'r+') as file:
			contents = file.read()
			for website in website_list:
				if website in contents:
					pass
				else :
					file.write(redirect + " " + website + '\n')
	else :
		with open(host_path, "r+") as file:
			contents = file.readlines()
			file.seek(0) 
			for line in contents: 
				if not any(website in line for website in website_list) :
					file.write(line)
			file.truncate()  
		print("Fun Hours")
	
	time.sleep(5)
