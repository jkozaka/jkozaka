apps = ["curse","times tables","fortune teller"]
def run():
    if idchoice == "1":
        curse()
        main_screen()
    elif idchoice == "2":
        times_tables()
        main_screen()
    elif idchoice == "3":
        fortune_teller()
        main_screen()
    else:
        main_screen()
def curse():
    print("i am your worst nightmare on all days i will haunt you")
    print("do you beg mercy yes or no?")
    mercy = input("type yes or no").lower()
    if mercy == "yes":
        print("there is no mercy in this world of code")
        print("because of your foolishness you derserve DEATH!!!!!")
        for DEATH in range(0,21):
            print("muderers,murdurers come this way!")
    if mercy == "no":
        print("you are smart because you know that there is no mercy in this world of code")
        print("you are out of my curse")
    #do not delete
    #final version
    #
    #
    #boo
def times_tables():
    for x in range(0,13):
        print(x,"x",12,"=",x*12)
    print("-----------------------------------------------------------------------")
    for z in range(0,13):
        print(z,"x",3,"=",z*3)
    running = "no"
def main_screen():
    number = 0
    for item in apps:
        number = number + 1
        print(number,")",item)
    global idchoice
    idchoice = input("choose app:")
    running = "yes"
    run()
def fortune_teller():
    import random
    yesno = ["yes","no"]
    print("i am the yes,no fortune teller")
    input("ask me a question ")
    print(random.choice(yesno))
main_screen()


