"""
Script by Binu Balan
Created on - 11 Nov 2021
Port validation
"""

import socket

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def query():
    print("--------------------------------------------")
    dadd = input("Enter the Server IP/Hostname : ")
    dport = int(input("Enter the port number : "))
    dest = (dadd,dport)
    socket.setdefaulttimeout(0.5)
    port_check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stat = port_check.connect_ex(dest)
    if stat == 0:
        print(bcolors.OKGREEN + "[ Success ]" + bcolors.ENDC,dadd," : Connection to port ",dport)
        port_check.close()
    else:
        print(bcolors.FAIL + "[ Failed ]" + bcolors.ENDC,dadd," : Connection to port ",dport)
        port_check.close()

def multiportquery():
    print("--------------------------------------------")
    dadd = input("Enter the Server IP/Hostname : ")
    dport = input("Enter the port number (comma separated) : ")
    # dest = (dadd,dport)
    dipport = dport.split(",")
    for eipport in dipport:
        dest = (dadd, int(eipport))
        socket.setdefaulttimeout(0.5)
        port_check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stat = port_check.connect_ex(dest)
        if stat == 0:
            print(bcolors.OKGREEN + "[ Success ]" + bcolors.ENDC,dadd," : Connection to port ",eipport)
            port_check.close()
        else:
            print(bcolors.FAIL + "[ Failed ]" + bcolors.ENDC,dadd," : Connection to port ",eipport)
            port_check.close()


def portping():
    print("--------------------------------------------")
    dadd = input("Enter the Server IP/Hostname : ")
    dport = int(input("Enter the port number : "))
    pcount = int(input("Enter the ping count : "))
    dest = (dadd,dport)
    Pass = 0
    Fail = 0
    for i in range(pcount):
        dest = (dadd, dport)
        socket.setdefaulttimeout(0.5)
        port_check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stat = port_check.connect_ex(dest)
        if stat == 0:
            print(i,".",bcolors.OKGREEN + "[ Success ]" + bcolors.ENDC,dadd," : Connection to port ",dport)
            port_check.close()
            Pass += 1
        else:
            print(i,".",bcolors.FAIL + "[ Failed ]" + bcolors.ENDC,dadd," : Connection to port ",dport)
            port_check.close()
            Fail += 1
    print("----------------------------")
    print("Total Success : ",Pass)
    print("Total Failure : ",Fail)
    print("----------------------------")


print("--------------------------------------------")
print("1. Query single IP and Single Port")
print("2. Query single IP and multiple Port")
print("3. Port ping")
print(" ")
opt = int(input("Select Option : "))
if opt == 1:
    query()
elif opt == 2:
    multiportquery()
elif opt == 3:
    portping()
else:
    print("No valid option selected.")
    print("Input value between 1-3 only.")


print("--------------------------------------------")
