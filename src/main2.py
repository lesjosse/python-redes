edad = None
permiso = None

while edad is None:
 try:
     edad = int(input("Ingrese su edad"))
     print(edad)
     permiso = input("Tiene permiso(Si/NO)")

     if edad < 18:
         print("programa terminado")
         break
     elif permiso == "Si":
         print("Puede Acceder")
     elif permiso == "No":
         print("No puede acceder")
 except ValueError:
        print("Error en los datos")