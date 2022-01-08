import random
import os
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
    randsq = square(random.randint(0,9) , random.randint(1,6))
class demominefield:
    for a in range(0,3):
        print(square(random.randint(0,9) , random.randint(1,6))
         + square(random.randint(0,9) , random.randint(1,6))
         + square(random.randint(0,9) , random.randint(1,6)))