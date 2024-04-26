#Parámetros por omisión

def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)

saludar('Pepona')


#Keywords como parámetros: Cargamos las vars cuando llamamos a la f:
def saludar(nombre, mensaje):
    print(mensaje, nombre)

saludar(nombre='Benito', mensaje='Hola')


#Parámetros arbitrarios:  es posible que una función, espere recibir un número arbitrario desconocidode argumentos.
#Estos argumentos, llegarán a la función en forma de tupla.
#Para definir argumentos arbitrarios en una función, se antecede al parámetro un asterisco (*):

def recorrer_parametros_arb(param_fijo, *param_arb):
    print(param_fijo)
    #Los parámetros arbitrarios se recorren como tuplas
    for argumento in param_arb:
        print(argumento)

recorrer_parametros_arb('Fijo', 'Arb1', 'Arb2', 'Arb3', 'Arb4')

#*****RECURSIVIDAD*****

#con while loop
i = 0
while i < 10:
    print(i, end='<')
    i += 1
print()    

#con RECURSIVIDAD
def f(i):
    if i < 10:
        print(i, end='<')
        f(i + 1)
f(1)
print()
f(-3)
print()


#◘◘◘Ejemplo: Contruir una f: que haga una pregunta y acepte 3 intentos usando recursividad


def jugar(intento):
    respuesta = int(input("Adiviná qué número estoy pensando:" ))
    if respuesta != 7:
        if intento < 3:
            print("Nop!!! Intentálo de nuevo...")
            intento += 1  #intento es un param. Se puede actualizar como una var cualquiera
            jugar(intento)
        else:
            print("Sorry!")
    else:
        print("Ganaste!!")

jugar(1)      