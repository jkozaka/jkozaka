import os
import time

#clears the terminal
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#for ansi escape sequences
esc = lambda code : "\033[" + str(code) + "m"

#animation player. uses a list to make an text animation
def animplay(frames,framedelay,repeat):
    for loop in range(0,repeat):
        for frame in frames:
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            print(frame)
            time.sleep(framedelay)