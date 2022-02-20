#✓
import os
os.chdir("/run/media/jkozaka/jkozaka/github/jkozaka/productivity") 

clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')#defines the function to clear terminal

def reload():
    remder = open("do_this.txt", "r").read() #the contents of the reminder list
    remders = remder.split("\n") #list of all different reminders. (expanded)
    remsplit = [] #list of lists(lists consist of title and details )
    expand = [] #list of reminders to expand (list ids)
    #creates empty lists

    for a in remders:
        remsplit.append(a.split(":"))
    #fills in remsplit

    clear

    for b in range(0,len(remsplit)):
        print(remsplit[b][0] + " : " + remsplit[b][2] if b in expand else remsplit[b][0])
    #lists out todo list

def editprompt():
    command = input(">>") #createst variable for command

reload()