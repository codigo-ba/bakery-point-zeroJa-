#4.C) Desarrollá un juego para adivinar un número al azar entre el 1 y el 100. Una vez que
#responde, se le dirá si ha acertado, se ha pasado o se ha quedado corto, y se le informará el
#número que salió. Se valora utilizar funciones.

from random import randint

azar = randint(1, 100)

num = int(input("Adiviná qué número entre el 1 y el 100 estoy pensando...: "))

while num < 1 and num > 100:
    num = int(input("Tiene que ser un número entre 1 y 100!. Intentalo de nuevo: "))
if num < azar:
    print("Te quedaste corto!")
elif num > azar:
    print("Te pasaste!")
else:
    print("Acertaste!")

print(f"Estaba pensando en número {azar}")