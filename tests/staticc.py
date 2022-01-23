import random
import os

esc = lambda code : "\033[" + str(code) + "m"

sq = lambda: esc(random.randint(42,46)) + "  " + esc(0)
while True:
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    for a in range(0,5):
        print(sq()+sq()+sq()+sq()+sq())