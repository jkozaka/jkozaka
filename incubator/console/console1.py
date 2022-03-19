import os

class functions: #defines functions
    global clear
    global esc
    clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    esc = lambda code : "\033[" + str(code) + "m"

class main: #main stuff
    clear
    while True:
        cmd = input(esc(42) + esc(1) + os. getcwd() + esc(46) + ">" + esc(0) + " ")
        os.system(cmd)