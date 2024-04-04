#6.B) Escribí un programa que simule las tiradas de un dado hasta que el usuario lo requiera. El usuario debe adivinar
#qué número salió optando por números del 1 al 6. El programa debe informar al finalizar: cantidad de tiradas, cantidad
#de aciertos y cantidad de errores

import random
tirada = input("Hacé tu tirada! Presioná 's' para comenzar!")
if tirada == "s":
    r = random.randint(1,6)
    adivinar = int(input("¿Qué número salió?: "))
    if adivinar == r:
        print("ACERTASTE!")
    else:
        print("NOP!")
sn = input("Otro tiro? 's' o 'n'?: ")
if sn == "n":
    print("Gracias! Adiós!")