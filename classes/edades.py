def main():
    respuesta = "S"
    while respuesta == "S":

        e = solicitar_edad()
        calc = calcular_rango_edad(e)
        respuesta = preg_continua()
    mostrar_resultados()

def solicitar_edad():
    edad = int(input("Edad: "))
    return edad

def calc(x):
    if x < 18:
        sum = 