# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. 
# Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
import time

datos = time.strftime("%H %M %S", time.localtime())
datos = datos.split(" ")
datos[0] = 4
datos[1] = 0
datos[2] = 0
if(int(datos[0]) >= 7):
    print("Es hora de ir a casa. El horario laboral ha finalizado.")
else:
    datos[0] = 6 - int(datos[0])
    datos[1] = 60 - int(datos[1])
    datos[2] = 60 - int(datos[2])

    if(datos[2] == 60):
        datos[2] = 0
        datos[1] += 1
    if(datos[1]>= 60):
        datos[0] += 1
        datos[1] =  0

    print("Todavia quedan %d:%d:%d para terminar el horario laboral." %(datos[0], datos[1], datos[2]))
