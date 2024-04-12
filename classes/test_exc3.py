#Escribir el código de las 5 funciones llamadas en este main:

def main():
    respuesta = "Yes"
    while respuesta == "Yes":
        op = preguntar_suma_o_promedio()  #sólo responder "suma" o "promedio"
        n1 = pedir_numero()  #puede tener decimales, no puede ser 0 o negativo
        n2 = pedir_numero()
        calculo = calcular(op, n1, n2) #calcular suma o promedio según la opción
        mostrar_mensaje(calculo, op)
        respuesta = preguntar_si_desea_seguir() # debe ser "Yes" o "No"
    print("final")

def preguntar_suma_o_promedio():
    opcion = input("Indique operación a realizar: suma o promedio: ").lower()
    while opcion != "suma" and opcion != "promedio":
        opcion = input("Entrada inválida. Debe indicar 'suma' o 'promedio': ")
    return opcion

def pedir_numero():
    n = float(input("Ingrese un número mayor a 0: "))
    while n <= 0:
        n = float(input("Entrada inválida. Debe ingresar un número mayor a 0: "))
    return n

def calcular(op, n1, n2):
    if op == "suma":
        sum = n1 + n2
        return sum
    else:
        prom = (n1 + n2)/2
        return prom
    
def mostrar_mensaje(calculo, op):
    print(f"El resultado de la operación {op} elegida es: {calculo}")

def preguntar_si_desea_seguir():
    respuesta = input("Desea realizar otra operación?. Indique 'Yes' o 'No': ").capitalize()
    while respuesta != "Yes" and respuesta != "No":
        respuesta = input("Entrada inválida. Debe responder 'Yes' o 'No': ").capitalize()
    return respuesta

main()
