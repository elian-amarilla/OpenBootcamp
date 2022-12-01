# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = ""
    nota = 0.0

    def cambiarNombre(self, nombre):
        self.nombre = nombre
    
    def cambiarNota(self, nota):
        self.nota = nota


alumno = Alumno()
alumno.cambiarNombre("Juan")
alumno.cambiarNota(7)

print("El alumno %s tiene una nota de %.2f" %(alumno.nombre, alumno.nota))
if(alumno.nota < 7):
    print("Esta desaprobado.")
else:
    print("Esta aprobado.")
