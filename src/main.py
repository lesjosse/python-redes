

numero = None

while numero is None:
    try:
        numero = int(input("Ingrese un número"))
        
        print("Número ingresado: ", numero)
        if numero == 0:
            print("Cero")
        elif numero >0:
            print("Positivo")
        else:
            print("Negativo")

    except ValueError:
        print("Error! Debes ingresar un número válido")


