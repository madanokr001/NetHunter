import socket
import os
import sys
from NetTools.nmap_script import *
from NetTools.spoof_script import *
from NetTools.help_script import *
from NetTools.dos_script import *
from NetTools.ping_script import *
from NetTools.sniff_script import *

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

terminal = TextColors.YELLOW + ">> " + TextColors.RESET

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.YELLOW + """
 _   _      _   _   _             _            
| \ | |    | | | | | |           | |           
|  \| | ___| |_| |_| |_   _ _ __ | |_ ___ _ __ 
| . ` |/ _ \ __|  _  | | | | '_ \| __/ _ \ '__|
| |\  |  __/ |_| | | | |_| | | | | ||  __/ |   
\_| \_/\___|\__\_| |_/\__,_|_| |_|\__\___|_| 

-- version 1.0 ---
-- github : github.com/madanokr001 --
-- Network Hacking Tools --

 -- usage --
   
 >> help
 >> nmap
 >> spoof 
 >> sniff
 >> dos
 >> ping
 >> exit

    """ + TextColors.RESET)

def main():
    while True:
        logo()
        select = input(TextColors.YELLOW + terminal + TextColors.RESET)

        if select == "help" or select.lower() == "help":
            helpmenu()
     
        elif select == "nmap" or select.lower() == "n":
            nmap()

        elif select == "ping" or select.lower() == "p":
            ping()

        elif select == "spoof" or select.lower() == "s":
            spoof()

        elif select == "sniff" or select.lower() == "sn":
            sniffer()
            
        elif select == "dos" or select.lower() == "d":
            dos()

        elif select == "exit" or select.lower() == "e":
            print(TextColors.CYAN +"[+] NetHunter EXIT..."+ TextColors.RESET)
            sys.exit()
    
             


if __name__ == "__main__":
    main()
            



    








