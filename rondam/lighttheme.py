import os

#bad bad bad

class functions: #defines functions
    global clear
    global esc
    clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    esc = lambda code : "\033[" + str(code) + "m"

class main: #main stuff
    while True:
        clear
        print(esc(7))
        cmd = input(os. getcwd() + " >")
        os.system(cmd)