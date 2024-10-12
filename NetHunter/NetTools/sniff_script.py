import socket
from scapy.all import *
import os
import sys
import time

class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    PURPLE = '\033[35m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = "\033[01;01m"
    DARK_RED = "\033[38;5;124m"
    CRIMSON = "\033[38;5;196m"
    TOMATO = "\033[38;5;202m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"

def sniffer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.YELLOW + """
  _____       _  __  __          
 / ____|     (_)/ _|/ _|         
| (___  _ __  _| |_| |_ ___ _ __ 
 \___ \| '_ \| |  _|  _/ _ \ '__|
 ____) | | | | | | | ||  __/ |   
|_____/|_| |_|_|_| |_| \___|_|                                   

-- version 1.0 --
-- packet sniffer menu --   
              
 -- usage --    
                       
 >> sniff                 
 >> exit
          
        """ + TextColors.RESET)

    while True:
        select = input(TextColors.YELLOW + ">> " + TextColors.RESET)

        if select == "sniff" or select.lower() == "s":
            global packet_count  # Add global here
            packet_count = 0

            def start_sniffing(target_ip):
                print(TextColors.YELLOW + f"[+] SNIFFING STARTED : {target_ip}"+ TextColors.RESET)
                pcap_file = sniff(prn=lambda x: process_packet(x, target_ip), filter=f"host {target_ip}")
                print(TextColors.YELLOW + f"[*] FINISHED SNIFFING : {target_ip}"+ TextColors.RESET)
                if packet_count == 0:
                    print(TextColors.RED + "[-] No Packets Captured"+ TextColors.RESET)
                    sys.exit()
                else:
                    print(TextColors.CYAN + f"[+] TOTAL : {packet_count}"+ TextColors.RESET)
                    file_name = input(TextColors.YELLOW + "[+] FILE NAME (.pcap): "+ TextColors.RESET)
                    wrpcap(file_name, pcap_file)

            def process_packet(packet, target_ip):
                global packet_count
                output = ""

                if ARP in packet:
                    arp_src_ip = packet[ARP].psrc
                    arp_dst_ip = packet[ARP].pdst
                    arp_op = "who has" if packet[ARP].op == 1 else "is at"
                    output = f"[+] ARP | Source : {arp_src_ip} | Destination : {arp_dst_ip} | {arp_dst_ip} {arp_op}"

                elif IP in packet:
                    src_ip = packet[IP].src
                    dst_ip = packet[IP].dst
                    ttl = packet[IP].ttl

                    if src_ip == target_ip or dst_ip == target_ip:
                        if packet[IP].proto == 1:
                            msg_type = packet[ICMP].type
                            code = packet[ICMP].code
                            output = f"[+] ICMP | Source : {src_ip} | Destination : {dst_ip} | TTL: {ttl} | Type : {msg_type} | Code : {code}"

                        elif packet[IP].proto == 6:
                            sport = packet[TCP].sport
                            dport = packet[TCP].dport
                            seq = packet[TCP].seq
                            ack = packet[TCP].ack
                            flags = packet[TCP].flags
                            output = f"[+] TCP | Source: {src_ip}:{sport} | Destination : {dst_ip}:{dport} | TTL : {ttl} | Seq : {seq} | Ack : {ack} | Flags : {flags}"

                        elif packet[IP].proto == 17:
                            sport = packet[UDP].sport
                            dport = packet[UDP].dport
                            udp_length = packet[UDP].len
                            output = f"[+] UDP | Source: {src_ip}:{sport} | Destination : {dst_ip}:{dport} | TTL : {ttl} | Length : {udp_length}"

                        elif packet.haslayer(Raw):
                            payload = packet[Raw].load.decode(errors='ignore')
                            if "HTTP" in payload:
                                output = f"[+] HTTP | Source : {src_ip} | Destination : {dst_ip} | Payload : {payload[:50]}..."

                        elif packet.haslayer(DNS):
                            dns_qr = "Query" if packet[DNS].qr == 0 else "Response"
                            dns_name = packet[DNS].qd.qname.decode() if DNS in packet else ""
                            output = f"[+] DNS | {dns_qr} | Source : {src_ip} | Destination : {dst_ip} | Name: {dns_name}"

                if output:
                    print(output)
                    packet_count += 1
                    time.sleep(0.5)

            target_ip = input(TextColors.YELLOW + "[+] ENTER THE IP : "+ TextColors.YELLOW)
            start_sniffing(target_ip)

        elif select == "exit" or select.lower() == "e":
            sys.exit()





