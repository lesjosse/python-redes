#ejercicios con elif.
#Programa para dar la nota final a un alummno.
nota = None

try:
    nota = int(input("Ingrese su nota"))
    faltas = int(input("Ingrese la cantidad de faltas"))
    if nota < 0 or nota > 5:
     print("La nota es de cero(0) a cinco(5)")
    elif faltas > 20:
       print("Reprobado por inasistencia!")
    elif nota < 3:
       print("Reprovado")
    elif nota > 3 and faltas <= 20:
       print("Aprobado!")
    else:
       print("Valores invalidos")

except ValueError:
    print("Error en los valores")

