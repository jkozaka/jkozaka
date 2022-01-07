import random
import os
class functions:
    global esc
    global square
    global clear
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    def esc(code):
        return "\033[" + str(code) + "m"
    def square(number, colour):
        colcod = colour + 40
        return esc(str(colcod)) + esc(4) + str(number) + "▐" + esc(0)
class presqs:
    global blanksq
    global randsq
    blanksq = square(" " ,7)
    randsq = square(random.randint(0,9) , random.randint(1,6))
for a in range(0,3):
    print(square(random.randint(0,9) , random.randint(1,6))
     + square(random.randint(0,9) , random.randint(1,6))
     + square(random.randint(0,9) , random.randint(1,6)))
print(blanksq)