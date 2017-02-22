print "funcion multiplicacion"
a = int(input("primer numero: "))
b = int(input("segundo numero: "))
def mul(lista):
    mul = 1
    for i in lista:
        mul *= i
    return mul
print "el resulatdo es: ", a * b
