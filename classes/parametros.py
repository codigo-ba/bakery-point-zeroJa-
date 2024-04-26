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
