#5.A) Diseñá un código para que la palabra hola aparezca en pantalla 5 veces, una por renglón. A continuación agregá el
#código para que aparezca 10 veces en el mismo renglón, separada por un espacio.

#Opción 2: Iterar con range()
for i in range(5):
    print("hola")

for i in range(10):
    print("hola", end=" ")
print()