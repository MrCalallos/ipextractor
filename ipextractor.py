from scapy.all import *

target_ip = '192.168.1.1/24' #escanea ips desde 192.168.1 hasta 192.168.1.255

#crear arp

#2 capa ARP
arp = ARP(pdst=target_ip)#IP


#3 capa ARP
ether = Ether(dst="ff:ff:ff:ff:ff:ff")#Extraer MAC

paquete = ether/arp

respuesta = srp(paquete,timeout=2,verbose=0)[0]

clients = []

for sent,received in respuesta:
    clients+=[[received.psrc,received.hwsrc]]
    
total_ips = len(clients)

for i in range(total_ips):
    print("IP : {}   MAC:{}".format(clients[i][0],clients[i][1]))

