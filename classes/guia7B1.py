#Idem 7B con opción a "DESEA CONTINUAR?"
#7B) Realizar un programa que cambie grados centígrados a grados Farenheit o Celsius (según la opción del usuario),
#utilizando funciones.

def main():
    respuesta = "S"
    while respuesta == "S":
        cent = solicitar_centigrados()
        tipo_unidad = solicitar_unidad()
        if tipo_unidad == "C":
            convert_cel = convertir_celsius(cent)
            print(convert_cel)
            print("El grado Celsius (°C) sustituyó desde 1948 como unidad de medida al grado centígrado.\nAmbas unidades son iguales en valor.")
        else:
            convert_fahr = convertir_fahrenheit(cent)
            print(convert_fahr)
        respuesta = preguntar_si_continua()
    print("Gracias por utilizar nuestro conversor :) !")


def solicitar_centigrados():
    c = float(input ("Ingrese los grados centígrados: "))
    return c

def solicitar_unidad():
    u = input("A qué unidad quiere convertir los grados centígrados? C = Celsius o F = Farenheit: ").upper()
    while u != "C" and u != "F":
        u = input("Opción Inválida. Debe ingresar 'C' o 'F': ").upper()
    return u
    
def convertir_celsius(grados_centigrados):
    return f"Los {grados_centigrados}°C ingresados equivalen a {grados_centigrados}° Celsius."
    
def convertir_fahrenheit(grados_centigrados):
    fahrenheit = (grados_centigrados * 9/5) + 32
    return f"Los {grados_centigrados}°C ingresados equivalen a {fahrenheit}° Fahrenheit."

def preguntar_si_continua():
    respuesta = input("Desea continuar? Ingrese 'S' o 'N': ").upper()
    while respuesta != "S" and respuesta != "N":
        respuesta = input("Entrada inválida. Debe ingresar 'S' o 'N': ").upper()
    return respuesta


if __name__ == "__main__":
    main()