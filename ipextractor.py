#Script published by Kalash0
#u need the scapy libary and npcap or this will not work :)

from scapy.all import *

target_ip = '192.168.1.1/24' #scan ip from 192.168.1 from 192.168.1.255

#create arp

#2 layer ARP
arp = ARP(pdst=target_ip)#IP


#3 layer ARP
ether = Ether(dst="ff:ff:ff:ff:ff:ff")#Extract MAC

packet = ether/arp

answer= srp(packet,timeout=2,verbose=0)[0]

clients = []

for sent,received in answer:
    clients+=[[received.psrc,received.hwsrc]]
    
total_ips = len(clients)

for i in range(total_ips):
    print("IP : {}   MAC:{}".format(clients[i][0],clients[i][1]))

