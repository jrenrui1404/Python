# Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
# de números primos que queremos mostrar.

import math
num = 0
cant_primos=0
while True:
    cant_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar:"))
    if cant_a_mostrar>0: break

while cant_a_mostrar > 0:
    num = num +1
    divisor = 1
    divisores = 0
    while divisor <= num:
        if num % divisor == 0:
            divisores = divisores+1
        divisor = divisor + 1
    if divisores == 2:
        cant_primos = cant_primos + 1
        print ("%d : %d" % (cant_primos,num))
        cant_a_mostrar = cant_a_mostrar - 1    