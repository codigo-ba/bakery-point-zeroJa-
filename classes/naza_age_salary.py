def main():
    # ingresar edad y sueldo
    edad = int(input("Ingrese la edad: "))
    sueldo = int(input("Ingrese sueldo"))
    print(clasificacion_edad(edad))

def clasificacion_edad(e):
    acumulador1 = 0
    acumulador2 = 0
    acumulador3 = 0
    acumulador4 = 0
    if e < 18:
        acumulador1 += 1
    elif 18 <= e <= 25:
        acumulador2 += 1
    elif 26 <= e <= 40:
        acumulador3 += 1
    else:
        acumulador4 += 1
    return acumulador1, acumulador2, acumulador3, acumulador4

main()