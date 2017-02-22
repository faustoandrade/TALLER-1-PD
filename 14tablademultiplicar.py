print "Tabla de multiplicar"

factor = int(raw_input("ingrese el numero que desea multiplicar: "))
rango = range(1, 11)

for elemento in rango:
    producto = factor * elemento
    print factor, " X ", elemento, " = ", producto
print "Tabla del: ", factor