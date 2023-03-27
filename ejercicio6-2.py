class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    aprobado = ""
    
    def aprobacion(self):
        if self.nota < 6:
            self.aprobado = "NO"
        return (self.aprobado)

    def __str__(self):
        return ("Alumno: {}, nota: {}, {} ha sido aprobado".format(self.nombre, self.nota, self.aprobado)) 

alumno = Alumno("Pepe Perez", 3)
alumno.aprobacion()
print(alumno)