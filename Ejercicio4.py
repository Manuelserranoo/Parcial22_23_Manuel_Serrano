import unittest

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        #añadir un print que diga si el alumno se ha creado con exito
        print("EL alumno",self.nombre, "se ha creado con éxito")
    def calificacion(self):
        if self.nota>=5:
            print(self.nombre,"ha aprobado")
        else:
            print(self.nombre,"ha suspendido")
    def __str__(self):
        return "Alumno: "+self.nombre+" Nota: "+str(self.nota)
    
#hacer los test de la clase Alumno
class TestAlumno(unittest.TestCase):
    def test_calificacion(self):
        alumno1=Alumno("Juan",7)
        alumno2=Alumno("Ana",3)
        alumno1.calificacion()
        alumno2.calificacion()
        self.assertEqual(alumno1.calificacion(),self.nombre,"ha aprobado")
        self.assertEqual(alumno2.calificacion(),self.nombre,"ha suspendido")
    
    

if __name__ == "__main__":
    alumno1=Alumno("Juan",7)
    alumno2=Alumno("Ana",3)
    print(alumno1)
    print(alumno2)
    alumno1.calificacion()
    alumno2.calificacion()