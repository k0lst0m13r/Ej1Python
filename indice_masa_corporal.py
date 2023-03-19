import math

peso = int(input("Ingrese su peso: ")) 
estatura = float(input("Ingrese su estatura en metros: "))

indice_masa_corporal = peso / estatura ** 2

print("Su indice de masa corporal es: ", round(indice_masa_corporal, 2))