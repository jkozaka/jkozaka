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
    print("\033[0m")
    loading = ["/","-","\\","|"]
    smile = ["╰(°▽°)╯","╭(°▽°)╮"]
    firework = [".","·","●","◉","◎","⠿","⠶","┅","…","_","_"]
    title = ["\033[32mt","te","tes","test","test ","test t","test ti","test tit","test titl","test title"]
    animplay(title,0.1,1)
