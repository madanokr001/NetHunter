import socket

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
    GOLD = '\033[38;5;214m'

def ping():
    
    print(TextColors.YELLOW + """
  _____ ______ _______   _____ _____  
 / ____|  ____|__   __| |_   _|  __ \ 
| |  __| |__     | |      | | | |__) |
| | |_ |  __|    | |      | | |  ___/ 
| |__| | |____   | |     _| |_| |     
 \_____|______|  |_|    |_____|_|     
       """+ TextColors.RESET)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        url = input(TextColors.YELLOW + "ENTER THE HOST : "+ TextColors.RESET)
        ip = socket.gethostbyname(url)
        print(TextColors.CYAN + f'HOST : {url} IP : {ip}'+ TextColors.RESET)
    except socket.gaierror:
        print(TextColors.RED + "[-] ERROR : NOT FOUND NAME"+ TextColors.RESET)
    except Exception as e:
        print(f"[-] ERROR : {e}")

    input()




