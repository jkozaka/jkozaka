import os
import time

#clears the terminal
clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#for ansi escape sequences
#sets ansi escape sequences
esc = lambda code : "\033[" + str(code) + "m" #add in print function

#animation player. uses a list to make an text animation
def animplay(frames,framedelay,repeat):
    for loop in range(0,repeat):
        for frame in frames:
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            print(frame)
            time.sleep(framedelay)

#makes a movie title like a console
def consoletitle(display,delay):
    title = ""
    for a in display:
        title = title + a
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print(title)
        time.sleep(delay)
