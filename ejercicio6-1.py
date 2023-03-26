class Vehiculo():
    color = "color"
    ruedas = 4
    puertas = 4


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 1500

  
coche = Coche()

print(coche.color)
print(coche.ruedas)
print(coche.puertas)
print(coche.velocidad)
print(coche.cilindrada)