#✓
import os
os.chdir("C:/Users/jonas/Documents/GitHub/jkozaka/productivity")
clear = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
remder = open("do_this.txt", "r").read()
remders = remder.split("\n")
remsplit = []
expand = [1]
clear
for a in remders:
    remsplit.append(a.split(":"))
for b in range(0,len(remsplit)):
    print(remsplit[b][0] if b in expand else remsplit[b][0] + " : " + remsplit[b][1])