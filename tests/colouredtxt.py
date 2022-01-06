def esc(code):
    return "\033["+ str(code) + "m"
colours = [30 , 31 ,32 ,33 ,34 ,35 ,36 ,37 ,90 ,91 ,92 ,93 ,94 ,95 ,96, 97]
for x in colours:
    print(esc(str(x)) + "banana" + esc(0))