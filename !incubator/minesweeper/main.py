import random
import os
import time
class functions:
    global esc
    global square
    global clear
    global blanksq
    global randsq
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    esc = lambda code : "\033[" + str(code) + "m"
    square = lambda number, colour: esc(str(colour + 40)) + esc(4) + str(number) + "▐" + esc(0)
    blanksq = square(" " ,7)
    randsq = lambda: square(random.randint(0,9) , random.randint(1,6))
while True:
    clear()
    print(randsq() +randsq() +randsq() +randsq()) ; print(randsq() +randsq() +randsq() +randsq())
    print(randsq() +randsq() +randsq() +randsq()) ; print(randsq() +randsq() +randsq() +randsq())
    time.sleep(0.1)