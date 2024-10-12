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

def helpmenu():
    print(TextColors.BOLD + """
NetHunter commands:

>> nmap   : Performs network exploration and port scanning.
>> sniff  : packet sniffer menu 
>> spoof  : arp spoofing or dns spoofing mode 
>> dos    : Performs a denial of service attack.
>> ping   : ping host a get ip address
>> exit   : Exits the program.

For more information on a specific command, please enter that command.
          """+ TextColors.RESET)


    input()