print "Longitud de una cadena"

cadena = raw_input("ingrese la palabra: ")
print cadena
def longitud_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print "la palabra contiene", longitud_cadena(cadena), "caracteres"
