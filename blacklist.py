from datetime import datetime
# Time Stamp: 13:00  - automation video for blacklisting websites    

# here we can add a feature to take input in registering time******
 
end_time = datetime(2024, 1, 1, 20)

sites_blocked = []

path_to_host = r"C:\Windows\System32\drivers\etc\hosts"

fallout_address = '127.0.0.1'

def blocked():
    if datetime.now() < end_time:
        print('Sites That are Blocked: ')
        with open(path_to_host, 'r+') as hostsfile:
            host_content = hostsfile.read()
            for sites in sites_blocked: 
                if sites not in host_content:
                    hostsfile.write(fallout_address + " " + sites + "\n")

    else:
        print("Unblock Sites") 
        with open(path_to_host, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(sites in line for sites in sites_blocked):
                    hostfile.write(line) 
            hostsfile.turncate()


if __name__ == "__main__":
       # 1. run manually
       # 2. cron job (Utilizing this, also with Oracle database) - The awesomeness of automation (Pythons playground)
       # 3. while True           
       blocked() 

# Need to have list of websites that need to be blocked - We will use domain names!!!



