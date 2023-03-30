class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        #añadir un print que diga si el alumno se ha creado con exito
        print("EL alumno",self.nombre, "se ha creado con éxito")
    def calificacion(self):
        if self.nota>=5:
            return(self.nombre,"ha aprobado")
        else:
            return(self.nombre,"ha suspendido")
    

if __name__ == "__main__":
    alumno1=Alumno("Juan",7)
    alumno2=Alumno("Ana",3)
    alumno1.calificacion()
    alumno2.calificacion()