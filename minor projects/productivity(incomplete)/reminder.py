#✓
import os
os.chdir("/run/media/jkozaka/jkozaka/github/jkozaka/productivity") 

expand = [] #list of reminders to expand (list ids)

clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')#defines the function to clear terminal

def reload():
    remder = open("do_this.txt", "r").read() #the contents of the reminder list
    remders = remder.split("\n") #list of all different reminders. (expanded)
    remsplit = [] #list of lists(lists consist of title and details )
    

    for a in remders:
        remsplit.append(a.split(":"))
    #fills in remsplit

    clear

    for b in range(0,len(remsplit)):
        print(remsplit[b][0] + " : " + remsplit[b][2] if b in expand else remsplit[b][0])
    #lists out todo list

def prmpt():
    def help():

        helpchs = input("available commands:\n1-add\n2-remove\n3-edit order\n4-edit reminders\n5-mark as done\n6-leave\n> ")
        #selects choice

        if helpchs == "6":
            exit()
        

    cmd = input(">> ") #createst variable for command
    help()

reload() #loads list
prmpt() #prompts  for command
