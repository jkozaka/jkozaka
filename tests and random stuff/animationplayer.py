import os
import time
class functions:
    global animplay
    def animplay(frames,framedelay,repeat):
        for loop in range(0,repeat):
            for frame in frames:
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                print(frame)
                time.sleep(framedelay)
class load:
    loading = ["/","-","\\","|"]
    smile = ["╰(°▽°)╯","╭(°▽°)╮"]
    firework = [".","·","●","◉","◎","⠿","⠶","┅","…","_","_"]
    animplay(loading,0.1,10)