import os
import time
def automate_task():
    print("[+] Protection Started")
    while True:
        #datas
        cmd = "netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r >ip_list.dat"
        ipslist=os.system(cmd)
        file1 = open('ip_list.dat', 'r')
        Lines = file1.readlines()
        for line in Lines:
            passing_data=line.strip()
            ip_data=passing_data.split()
            maximum_connection=open("maximum_connections.dat", "r")
            connection_count=maximum_connection.read()
            if(int(ip_data[0]) > int(connection_count)):
                ip_address=ip_data[1];
                command="sudo iptables -A INPUT -s "+ip_address+" -j DROP"
                os.system(command)
                print('[+]'+ip_address+'    Blocked from your server')
            else:
                print('[+] Secure')
            time.sleep(60)
