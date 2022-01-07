import os
import time
class functions:
    global esc
    global square
    global clear
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    def esc(code):
        return "\033[" + str(code) + "m"
class main:
    while True:
        print(esc(1) + esc(31))
        clear()
        print("/")
        time.sleep(0.1)
        clear()
        print("-")
        time.sleep(0.1)
        clear()
        print("\\")
        time.sleep(0.1)
        clear()
        print("|")
        time.sleep(0.1)