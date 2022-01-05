def esc(code):
    return "\033["+ str(code) + "m"
temp = esc(42) + esc(30) + esc(1) + "app fixe" + esc(0)
print(temp.center(50) + "\n")
print(esc(4) + esc(34) + "Escolha Um" + esc(0))