
import pygame as pg

import os
pg.init()
def splash(secs):
    texty = None
    splash = pg.display.set_mode([600,350],vsync=1)
    splash.fill([40,40,40])

    pg.draw.ellipse(splash, "yellow", [[50,100],[500,150]])
    pg.draw.ellipse(splash, "yellow", [[100,25],[400,300]])

    lfont = pg.font.Font("assets/fonts/thicc.ttf",56, bold=True)
    text = lfont.render("Lemon Engine", True, "gray")
    splash.blit(text,[1,250])

    ifont = pg.font.Font("assets/fonts/comf.ttf",28,)
    texty = ifont.render("welcome to", True, "darkgray")
    splash.blit(texty,[1,225])

    pg.display.flip()
    pg.time.delay(secs*1000)
def fileselect():
    def fsmain():
        filek = ""
        while filek != "y":
            file = input("Please write the adress of your game directory:\n--- ").replace("\\","/")
            fileko = input("Is your directory "+file+"?\ny/n : ").lower()
            filek = fileko[0]
        filel = file.split("/")
        sofar = []
        for diry in range(0,len(filek)):
            dire = filel[diry]
            if diry == 0 and dire[1] ==":":
                os.chdir(dire.upper())
                print(os.getcwd())
                dbase = None
                pass
            elif diry == 0 and dire[1] !=":":
                os.chdir('C:')
                dbase = None
            else:
                dbase = "/".join(sofar)
            print(os.listdir("C:"))
            if dire in os.listdir(dbase):
                pass
            else:
                print("NONEXISTENT DIRECTORY\n ")
                fsmain()

            if diry == 0 and dire[1] !=":":
                sofar.append(dire)

            print("sofar")
        if os.listdir(file) == []:
            print()
        else:
            print("DIRECTORY NOT EMPTY\n")
    fsmain()
fileselect()
#youcaneditdirectlyfromgithub
