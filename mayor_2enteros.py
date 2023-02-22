# input

X = int(input("ingrese un numero de X: "))

Y = int(input("ingrese el numero de Y: "))

# processing

if X > Y:
    msj = " es mayor que "

elif X < Y:
    msj = " es menor que "

else:
    msj = " es igual a "

# output

print("EL NUMERO: " + str(X) + msj + str(Y))