for i in range(6,12,3): # i toma valores desde 6 hasta 12(no incluído) y salta de a 3: 6, 9
    for j in range(i,0,-2): # j toma valores desde i hasta 0(no incluído) y salta de a 2 en reversa
        a = i - j
        print(a, end="")
    print()
print("Adiós")  

# Justificar el muestreo de pantalla via Prueba de escritorio
"""for i in range(4,16,4): 
    for j in range(i,0,-2): 
        a = i - j
        print(a, end="")
    print()
print("Bye!")  
"""