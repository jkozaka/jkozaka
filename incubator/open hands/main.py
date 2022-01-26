esc = lambda code : "\033[" + str(code) + "m"
print(esc(41) + "banana" + esc(0))