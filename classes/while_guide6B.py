#6.B) Escribí un programa que simule las tiradas de un dado hasta que el usuario lo requiera. El usuario debe adivinar
#qué número salió optando por números del 1 al 6. El programa debe informar al finalizar: cantidad de tiradas, cantidad
#de aciertos y cantidad de errores

import random

tirada = input("Hacé tu tirada! Presioná 's' para comenzar!")
total = 0
aciertos = 0
errores = 0
r = random.randint(1,6)

while tirada == "s":
    total += 1
    adivinar = int(input("¿Qué número salió?: "))
    if adivinar == r:
        aciertos += 1
        print("ACERTASTE!")
    else:
        errores += 1 
        print("NOP!")
    tirada = input("Otro tiro? 's' o 'n'?: ")
    
print(f"Total de Tiradas: {total} \nTotal de Aciertos: {aciertos} \nTotal de Errores: {errores} \nGracias! Adiós!")