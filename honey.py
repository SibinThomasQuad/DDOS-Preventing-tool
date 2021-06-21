import os
os.system("clear")
banner = open("banner.dat", "r")
print(banner.read())
def un_block():
    ip_address=input("Enter IP Address That you want to block:")
    command="iptables -D INPUT -s "+ip_address+" -j DROP"
    os.system(command)
    print('[+]'+ip_address+'    UnBlocked from your server')
    main()
def list_banned():
    os.system("iptables -L INPUT -v -n")
    main()
def ip_block():
    ip_address=input("Enter IP Address That you want to block:")
    command="sudo iptables -A INPUT -s "+ip_address+" -j DROP"
    os.system(command)
    print('[+]'+ip_address+'    Blocked from your server')
    main()
def ditect_ddos():
    #lines
    cmd = "netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r >ip_list.dat"
    ipslist=os.system(cmd)
    file1 = open('ip_list.dat', 'r')
    Lines = file1.readlines()
    print("----Result------")
    for line in Lines:
        passing_data=line.strip()
        ip_data=passing_data.split()
        flag=0
        maximum_connection=open("maximum_connections.dat", "r")
        connection_count=maximum_connection.read()
        if(int(ip_data[0]) > int(connection_count)):
            flag=1
            alert="(Flood Requests)"
        else:
            alert=''
        print('[+] IP Address:'+ip_data[1]+' \n  REQUEST:'+ip_data[0]+alert)
    if(int(flag) < 0):
        print("Result:No DDOS Ditected")
    else:
        print("Result:DDOS Ditected")
    main()
def main():
    print("DDOS Prevent tools")
    print("[1] Ditect DDOS [List Ip address that connected]")
    print("[2] Block IP Address")
    print("[3] List Blocked IP Address")
    print("[4] UnBlock IP Address")
    print("[0] Exit")

    option = input("Select Option:")
    if(int(option) == 1):
        ditect_ddos()
    if(int(option) == 2):
        ip_block()
    if(int(option) == 3):
        list_banned()
    if(int(option) == 4):
        un_block()
    if(int(option) == 0):
        print("Exiting...")
        quit()
main()
