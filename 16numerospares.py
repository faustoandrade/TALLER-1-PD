print "Numeros pares"

def cuentaPares(inNum):
    if not (inNum / 10):
        return 1 - (inNum % 2)
    else:
        newNum = inNum / 10
        return 1 - ((inNum % 10) % 2) + cuentaPares(newNum)

if __name__ == "__main__":
    num = input("Introduzca los numeros: ")
    print "El numero tiene ", cuentaPares(num), " numeros pares"
    raw_input()