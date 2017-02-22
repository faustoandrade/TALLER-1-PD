print "funcion suma"
a = int(input("primer numero: "))
b = int(input("segundo numero: "))
def sum(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
print "el resulatdo es: ", a + b
