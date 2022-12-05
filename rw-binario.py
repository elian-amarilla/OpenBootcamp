# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    nombre = ""
    modelo = ""
    tipo = ""
    encendido = False

    def __init__(self, nombre, modelo, tipo):
        self.nombre = nombre
        self.modelo = modelo
        self.tipo = tipo

    def arrancar(self):
        if(self.encendido == False):
            print("...  Arrancando el vehiculo ...")
            print("... Rrrunnnn ...")
            print(" Vehiculo encendio con exito.")
            self.encendido = True
        else:
            print("El vehiculo ya esta encendido.")



vehiculo1 = Vehiculo("Ford Fiesta", "2015", "Sedan")

f = open('datos.bin', 'r+b')
pickle.dump(vehiculo1, f)
f.close()

f = open('datos.bin', 'r+b')
carga = pickle.load(f)
f.close()

print(vehiculo1)
print(carga)
