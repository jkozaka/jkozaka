import random
import time
class functions:
    global esc
    global square
    def esc(code):
        return "\033[" + str(code) + "m"
    def square(number, colour):
        colcod = colour + 40
        return esc(str(colcod)) + esc(4) + str(number) + "▐" + esc(0)
for a in range(0,3):
    print(square(random.randint(0,9) , random.randint(1,6))
     + square(random.randint(0,9) , random.randint(1,6))
     + square(random.randint(0,9) , random.randint(1,6)))
blanksq = print(square(" " ,7))
blanksq
time.sleep(1)