#5.C) Diseñá un código que muestre la tabla de multiplicar de un número del 1 al 10 ingresado por el usuario. Si el
#usuario ingresa un número fuera de ese rango debe mostrar la palabra “error”.

def main():
    num = int(input("Ingresá un número del 1 al 10 para conocer su tabla: "))
    if 0 < num <= 10:
        tabla(num)
    else:
        print("Error")

def tabla(n):
    print(f"La tabla de {n} es:")
    for i in range(11):
        print(f"{n} * {i} = {n*i}")
    print()

if __name__ == "__main__":
    main()