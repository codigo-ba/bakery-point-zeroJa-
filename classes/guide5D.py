#5.D) Escribí un programa que pida un número de dados y muestre los valores de ese número de dados, al azar.

import random

def main():
    dados = int(input("Ingresá cuántos dados querés jugar: "))
    valor = tirada(dados)
    print(f"El valor total de la tirada es: {valor}")

def tirada(d):
    acum = 0
    for i in range(d):
        r = random.randint(1, 6)
        print(r)
        acum = acum + r 
    return acum 
if __name__ == "__main__":
    main()
