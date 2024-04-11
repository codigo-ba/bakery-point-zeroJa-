#2) En una empresa se ingresan edades y sueldos correspondientes a una cierta cantidad de empleados ingresados
#previamente.
#Se desea conocer cuántos empleados tienen e/ 18 y 25 años, cuantos e/ 26 y 40, cuántos >40, y cuántos < de edad.
#Se desea conocer el sueldo promedio.

def main():
    edad = solicitar_edad()
    sueldo = solicitar_sueldo()
    continuar = preguntar_si_continua()

def solicitar_edad():
    e = int(input("Ingrese edad: "))
    return e

def solicitar_sueldo():
    s = int(input("Ingrese sueldo: "))
    return s

def preguntar_si_continua():
    respuesta = input("Desea continuar ingresando? S/N: ").upper()
    while respuesta != "S" and respuesta != "N":
        respuesta = input("Debe ingresar S o N: ")
    return respuesta


def edad():
    
    if e < 18:
        menor += 1
    elif 18 <= e <= 25:
        e1 += 1
    elif 26 <= e <= 40:
        e2 += 1
    else:
        mayor += 1
    return menor, e1, e2, mayor
