print "Es vocal"

letra = raw_input("ingrese la vocal: ")
print letra
def vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

print "la vocal es: ", vocal(letra)