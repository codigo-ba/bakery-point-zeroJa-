
def main():
    contador_empleados = 0
    sueldo_acumulado = 0
    menor, e1, e2, mayor = 0, 0, 0,0
    respuesta = "S"
    while respuesta == "S":
        contador_empleados += 1
        edad = solicitar_edad()
        sueldo = solicitar_sueldo()
        sueldo_acumulado += sueldo
        edades = evaluar_edad(edad, menor, e1, e2, mayor)
        menor, e1, e2, mayor = edades
        sueldo_promedio = calcular_sueldo_promedio(contador_empleados, sueldo_acumulado)
        respuesta = preguntar_si_continua()
    mostrar_resultados(edades, sueldo_promedio)
    print("Fin")
        

def solicitar_edad():
    e = int(input("Ingrese edad: "))
    return e

def solicitar_sueldo():
    s = int(input("Ingrese sueldo: ")) 
    return s

def evaluar_edad(e, menor, e1, e2, mayor):
    
    if e < 18:
        menor += 1
    elif 18 <= e <= 25:
        e1 += 1
    elif 26 <= e <= 40:
        e2 += 1
    else:
        mayor += 1

    return menor, e1, e2, mayor
    #return f"Menores de 18: {menor}. Entre 18 y 25: {e1}. Entre 26 y 40: {e2}. Mayores de 40: {mayor}"

def calcular_sueldo_promedio(contador_empleados, sueldo_acumulado):
    promedio = sueldo_acumulado/contador_empleados
    return promedio

def preguntar_si_continua():
    respuesta = input("Desea continuar ingresando? S/N: ").upper()
    while respuesta != "S" and respuesta != "N":
        respuesta = input("Debe ingresar S o N: ")
    return respuesta

def mostrar_resultados(edades, sueldo_promedio):
    print(edades)
    print(f"El sueldo promedio es: {sueldo_promedio}")

main()