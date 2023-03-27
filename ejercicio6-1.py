class Vehiculo():

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad_max, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad_max = velocidad_max
        self.cilindrada = cilindrada
    def __str__(self):
        return "color {}, {}km/h, {} ruedas, {} puertas, {}cc".format(self.color, self.velocidad_max, self.ruedas, self.puertas, self.cilindrada)

class Camion(Vehiculo):
    def __init__(self, color, ruedas, puertas, carga_max, tipo_de_acoplado):
        super().__init__(color, ruedas, puertas)
        self.carga_maxima = carga_max
        self.tipo_de_acoplado = tipo_de_acoplado
    def __str__(self):
        return ("color {}, {} ruedas, {} puertas, {}kg, acoplado tipo {}".format(self.color, self.ruedas, self.puertas, self.carga_maxima, self.tipo_de_acoplado))

coche = Coche("Rojo", 4, 2, 180, 2100)
camion = Camion("Naranja", 22, 2, 30000, "Playo")

print(coche)
print(camion)