print ("Mas de tres")
a = int(input("primer numero: "))
b = int(input("segundo numero: "))
c = int(input("tercer numero: "))

if a>b and a>c:
    print ("el numero mayor es:", a)
elif b>a and b>c:
            print ("el numero mayor es:", b)
elif c>a and c>b:
            print ("el numero mayor es:", c)
else:
    print "son iguales"
