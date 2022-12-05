# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo.
#  Para ello, tendréis que acceder dos veces al archivo creado.

def crearArchivo(archivo, lista):
    for linea in lista:
        if not linea.endswith("\n"):
            linea += "\n"
        archivo.write(linea)

def leerArchivo(archivo):
    print("\n\nLectura del archivo: ")
    datos = archivo.read()
    print(datos)

lista = ["Escribiendo dentro del archivo", "algunas lineas, con tal de rellenarlo", "Muchas gracias por su tiempo."]
f = open("archivo.txt", "r+")
crearArchivo(f, lista)
leerArchivo(f)
f.close()
