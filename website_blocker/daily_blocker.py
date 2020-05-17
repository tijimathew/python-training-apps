import time
from datetime import datetime as dt
# Open the hosts file from C:\Windows\System32\drivers\etc
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.linkedin.com", "linkedin.com"]

is_work_hours = False 

# continously check if it is work hours or off-work hours
# Only update the hosts file at the beginning of the time window and only check for the time
# every 300 seconds
while True:
    cdt = dt.now()

    if dt(cdt.year, cdt.month, cdt.day, 8, 30) < cdt < dt(cdt.year, cdt.month, cdt.day, 19, 11):
        if is_work_hours == False:
            print("Working Hours In session")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write("\n" + redirect + " " + website)
            is_work_hours = True
        else:
            #print('Passing Work Hours')
            pass # do nothing if work hours is true
    else:
        if is_work_hours == True:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print("Fun Hours")
            is_work_hours = False
        else:
            #print('Passing Fun Hours')
            pass

    time.sleep(300)