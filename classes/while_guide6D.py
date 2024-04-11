#6.D) Escribí un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no
#sea mayor que el primero. El programa terminará escribiendo los dos números.

print("NÚMERO MAYOR")
print()
n = int(input("Escriba un número: "))
m = int(input(f"Escriba un número mayor que {n}: " ))
while m <= n:
    m = int(input(f"{m} no es mayor que {n} Inténtelo de nuevo: " ))
print(f"Los números que ha escrito son: {n} y {m}") 