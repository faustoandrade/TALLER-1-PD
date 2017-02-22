print "CANT DIGITOS"

cadena = raw_input("Escribe una cantidad de numeros: ")
while cadena != "":
    digitos = 0
    anterior = 0
    for numero in cadena:
        if numero >= '0' and numero <= '9':
            digitos += 1
        if numero in cadena[len(numero) - 1] >= '0' and numero <= '9':
            anterior += 1

    total = digitos - anterior
    print cadena
    print "NUMEROS: ", total + 1
    cadena = raw_input("Escribe una cantidad de numeros: ")

