import time
# Open the hosts file from C:\Windows\System32\drivers\etc
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.linkedin.com", "linkedin.com"]

while True:
    # continously check if it is work hours or off-work hours
    print(1)
    time.sleep(5)