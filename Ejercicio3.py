import unittest

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        #añadir un print que diga si el alumno se ha creado con exito
        print("EL alumno",self.nombre, "se ha creado con éxito")
    def calificacion(self):
        if self.nota>=5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")
    
#hacer los test de la clase Alumno


if __name__ == "__main__":
    alumno1=Alumno("Juan",7)
    alumno2=Alumno("Ana",3)
    alumno1.calificacion()
    alumno2.calificacion()
