import time
import os
def consoletitle(display,delay):
    title = ""
    for a in display:
        title = title + a
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print(title)
        time.sleep(delay)


consoletitle("weed shop 4:20",0.01)
