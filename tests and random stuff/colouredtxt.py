import os
import time
class functions:
    global esc
    global square
    global clear
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    esc = lambda code: "\033[" + str(code) + "m"
class main:
    while True:
        clear()
        print(esc(1) + esc(31) + "/" + esc(0))
        time.sleep(0.1)
        clear()
        print(esc(1) + esc(31) + "-" + esc(0))
        time.sleep(0.1)
        clear()
        print(esc(1) + esc(31) + "\\" + esc(0))
        time.sleep(0.1)
        clear()
        print(esc(1) + esc(31) + "|" + esc(0))
        time.sleep(0.1)