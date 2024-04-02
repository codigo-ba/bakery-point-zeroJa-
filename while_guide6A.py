#6.A) Diseñá un programa que imprima el promedio de los 30 primeros números múltiplos de 3. Realizar dos versiones
#del mismo programa: una que use la estructura while y otra versión que use ciclo for.

i = 1
suma = 0
while i <= 30:
    suma = suma + (i*3)
    i +=1
print(f"El promedio es: {suma/30}")
print()

print("Ahora con ciclo FOR")
suma = 0
for i in range(1, 31):
    suma = suma + (i*3)
print(f"El promedio también es: {suma/30}")


