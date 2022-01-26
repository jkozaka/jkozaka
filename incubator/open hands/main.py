import os
import random
class functions:
    global clear ;global esc
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    esc = lambda code : "\033[" + str(code) + "m"

