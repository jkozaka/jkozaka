
import os

class functions: #defines functions
    global clear
    global esc
    clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    esc = lambda code : "\033[" + str(code) + "m"
class main: #main stuff
    clear
    os.chdir("/")
    while True:
        print(esc(37))
        cmd = input(esc(42) + esc(1) + os. getcwd() + " " +
        esc(46) + ">" + #command prompt
        esc(0) + esc(36) + "▓▒░" + esc(0) + " " + esc(37))
        if cmd == "quit":
		        exit() #to exit app
        if cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
        os.system(cmd)