#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self. ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
fordFiesta = Coche("bordo", 4, 4, 215, 20);
print("Caracteristicas del coche: ")
print("Color: %s\t Cant. ruedas: %d\t Cant. puertas: %d" %(fordFiesta.color, fordFiesta.ruedas, fordFiesta.puertas))
print("Velocidad maxima %d KM/H\t Cilindrada %d" %(fordFiesta.velocidad, fordFiesta.cilindrada))
