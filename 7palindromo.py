print "palindromo"

letra = raw_input("ingrese la palabra: ")
print letra
def palindromo(palabra):
    x = -1
    y = 0

    for i in range(len(palabra)/2):
        if palabra[y] == palabra[x]:
            y = y + 1
            x = x - 1
        return True
    else:
        return False

print "la palabra es: ", range(len(palindromo)/2)

