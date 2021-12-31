def generate(smoothness):
    import random
    import statistics
    rand = []
    smooth = []
    for a in range(0,100):
        rand.append(random.randint(0,10))
    if smoothness > 0:
        for c in range(0, smoothness):
            smooth = []
            for b in range(0,100):
                lsides = [10,20,30,40,50,60,70,80]
                rsides = [19,29,39,49,59,69,79,89]
                usides = [1,2,3,4,5,6,7,8]
                dsides = [91,92,93,94,95,96,97,98]
                lucorners = [0]
                rucorners = [9]
                ldcorners = [90]
                rdcorners = [99]
                around = [rand[b], rand[b-1], rand[b+9], rand[b+10],
                rand[b +11], rand[b +1], rand[b-9], rand[b-10], rand[b-11]]
                lside = [rand[b +1], rand[b +11], rand[b-9]]
                rside = [rand[b-1], rand[b-11], rand[b+9]]
                uside = [rand[b-9], rand[b-10], rand[b-11]]
                dside = [rand[b+9], rand[b+10], rand[b+11]]
                lucorn = []
                rucorn = []
                ldcorn = []
                rdcorn = []
                def egde(location):
                    pass
                if not b in lsides and not b in rsides and not b in usides and not b in dsides and not b in lucorners and not b in rucorners and not b in ldcorners and not b in rdcorners:
                    pass
                elif b in lsides:
                    pass
                elif b in rsides:
                    around = [rand[b], rand[b]-1, rand[b]+9, rand[b]+10,
                    rand[b]-10, rand[b]-11]
                elif b in dsides:
                    around = [rand[b], rand[b]-1,
                    rand[b]+1, rand[b]-9, rand[b]-10, rand[b]-11]
                elif b in usides:
                    around = [rand[b], rand[b]-1, rand[b]+9, rand[b]+10, rand[b]+11,
                    rand[b]+1]
                elif b in lucorners:
                    around = [rand[b], rand[b]+10, rand[b]+11, rand[b]+1]
                elif b in rucorners:
                    around = [rand[b], rand[b]-1, rand[b]+9, rand[b]+10]
                elif b in ldcorners:
                    around = [rand[b], rand[b]-10]
                elif b in rdcorners:
                    around = [rand[b], rand[b]-1, rand[b]+1, rand[b]-9, rand[b]-10, rand[b]-11]
                smooth.append(statistics.mean(around))
            rand = smooth
        else:
            smooth = rand
    return smooth
def render(map):
    import pygame
    pygame.init()
    renwin = pygame.display.set_mode(size=[500,500], vsync=1)
    if len(map) == 1000:
        for y in range(0,10):
            nowy = x*50
            for x in range(0,10):
                nowx = y*50
    else:
        print("map tuple too short. must be 100 long")
print(generate(1))