#El factorial de un número natural se define como el producto de todos los números naturales hasta el mismo. Por
#ejemplo:
#Factorial de 5 = 5! = 5*4*3*2*1 = 120
#Factorial de 11 = 11! = 11*10*9*8*7*6*5*4*3*2*1 = 39.916.800
#El único caso especial es el caso del 0: 0! = 1
#Realizá un código que calcule el factorial de cualquier número que el usuario desee (sin usar la función factorial de la
#librería math) y lo muestre en pantalla con el siguiente formato, por ejemplo: 6 ! = 720


n = int(input("Ingresá n# para calcular el factorial: "))
c = n #podría usar n,  sin definir c, pero a la hora de imprimir, necesito el valor del input
if n != 0:
    for i in range(n - 1, 1, -1):
        c = c * i
    print(f"{n} ! = {c}")
else:
    print("0 ! = 1")


    
