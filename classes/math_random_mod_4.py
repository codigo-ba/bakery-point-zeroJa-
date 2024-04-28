#4.A) Sin ejecutar el código respondé: ¿Qué hace el siguiente programa?. Comprobá luego en la ejecución

from random import choice
A=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
print (choice(A),end="")
B=["♠","♣","♥","♦"]
print (choice(B))

#4.B) Diseñá el juego de la moneda para que el usuario adivine si sale cara o ceca (¡Sí!, se escribe
#con “c” https://dle.rae.es/ceca)

print("-----4.B) Cara o Ceca?-----")
print()
#---->choice() fué importado en ej 4A
respuesta = "S"
while respuesta == "S":
    moneda = ["CARA", "CECA"]
    azar = choice(moneda)
    tirada = input("Elegí, CARA o CECA?: ").upper()
    while tirada != "CARA" and tirada != "CECA":
        tirada = input("Entrada inválida, tenés que ingresar 'CARA' o 'CECA': ").upper()
    if tirada == azar:
        print(f"Acertaste! La la tirada fué {azar}!!")
    else:
        print(f"Ups!! La tirada fué {azar}")
    respuesta = input("Otra tirada? S o N: ").upper()
print("Gracias por jugar conmigo :8")
