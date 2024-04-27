#7B) Realizar un programa que cambie grados centígrados a grados Farenheit o Celsius (según la opción del usuario),
#utilizando funciones.
#Para convertir Fahrenheit a grados centígrados: restar 32 y luego multiplicar por 5/9 o 0,555.
#Para convertir grados centígrados a Fahrenheit: multiplicar por 9/5 o por 1,8 y luego sumar 32.
#Grados centígrados = (grados Fahrenheit − 32) × 5/9. Grados Fahrenheit = (grados centígrados × 9/5) +32.
#El grado Celsius (°C) sustituyó desde 1948 como unidad de medida al tradicionalmente conocido como grado centígrado,
#aunque ambas unidades son iguales en valor.


def main():
    cent = solicitar_centigrados()
    tipo_unidad = solicitar_unidad()
    if tipo_unidad == "C":
        convert_cel = convertir_celsius(cent)
        print(convert_cel)
        print("El grado Celsius (°C) sustituyó desde 1948 como unidad de medida al grado centígrado.\nAmbas unidades son iguales en valor.")
    elif tipo_unidad == "F":
        convert_fahr = convertir_fahrenheit(cent)
        print(convert_fahr)
    else:
        print(tipo_unidad)
        print("Ha ocurrido un ERROR")

def solicitar_centigrados():
    c = float(input ("Ingrese los grados centígrados: "))
    return c

def solicitar_unidad():
    u = input("A qué unidad quiere convertir los grados centígrados? C = Celsius o F = Farenheit: ").upper()
    while u != "C" and u != "F":
        u = input("Entrada inválida. Debe ingresar 'C' o 'F': ").upper()
    return u
    
def convertir_celsius(grados_centigrados):
    return f"Los {grados_centigrados}°C ingresados equivalen a {grados_centigrados}°Celsius."
    
def convertir_fahrenheit(grados_centigrados):
    fahrenheit = (grados_centigrados * 9/5) + 32
    return f"Los {grados_centigrados}°C ingresados equivalen a {fahrenheit}°Fahrenheit."

if __name__ == "__main__":
    main()