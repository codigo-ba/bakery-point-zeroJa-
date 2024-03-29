#5.B) Creá un programa que muestre una escala desde el 0 hasta un valor elegido por el usuario. El salto de la escala
#también lo decide el usuario.

escala = int(input("Ingrese Valor Final de la escala: "))
salto = int(input("Ingrese salto: "))

for i in range(0,escala,salto):
    print(i)