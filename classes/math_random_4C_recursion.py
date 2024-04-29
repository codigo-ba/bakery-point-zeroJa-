#4.C) Se valora utilizar RECURSIÓN DE FUNCIONES o LLAMADAS INTERNAS. Desarrollá un juego para adivinar un número al azar entre el 1 y el 100. Una vez que
#responde, se le dirá si ha acertado, se ha pasado o se ha quedado corto, y se le informará el
#número que salió. 

from random import randint

def main():
    num_random = generar_num()
    num_usuario = pedir_numero()
    validar_entrada = validar_num_usuario(num_usuario)
    validar_res = validar_resultado(num_random, validar_entrada)
    mostrar_resultado(validar_res, num_random)
    preguntar_si_continua()

def generar_num():
    azar = randint(1, 100)
    return azar

def pedir_numero():
    num = int(input("Adiviná qué número entre el 1 y el 100 estoy pensando...: "))
    return num

def validar_num_usuario(num):
    while num < 1 or num > 100:
        num = int(input("Tiene que ser un número entre 1 y 100!. Intentalo de nuevo: "))
    return num

def validar_resultado(num_r, entrada):
    if entrada < num_r:
        return "Te quedaste corto!"
    elif entrada > num_r:
        return "Te pasaste!"
    else:
        return "Acertaste!"

def mostrar_resultado(resultado, num_azar):
    print(resultado)
    print(f"Estaba pensando en el número {num_azar}")

def preguntar_si_continua():
    respuesta = input("Jugamos otra vez? S/N: ").upper()
    if respuesta != "S" and respuesta != "N":
        preguntar_si_continua()
    elif respuesta == "S":
        main()
    else:
        print("Gracias!!!")


if __name__ == "__main__":
    main()