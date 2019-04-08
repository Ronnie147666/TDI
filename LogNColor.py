from colorama import init,Fore, Back, Style
import platform, re

if (platform.system()=="Windows"):
    init(convert=True)

def setColor(color):
    print colors[color]

def Printer(output):
    print Style.BRIGHT+output


colors = {

    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
 
    

    }

def splitWords(word):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", word)
    

##Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
##Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
##Style: DIM, NORMAL, BRIGHT, RESET_ALL




