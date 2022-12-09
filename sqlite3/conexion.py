# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto 
# y la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3 as db

def crearTabla(nombre):
    conn = db.connect("mibase.db")
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {nombre}(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL);")
    cursor.close()
    conn.close()

def cargarRegistros(lista):
    conn = db.connect("mibase.db", isolation_level=None)
    cursor = conn.cursor()
    for id,nombre,apellido in lista:
        print(id, nombre, apellido)
        query = f"INSERT INTO alumnos VALUES({id}, '{nombre}', '{apellido}');"
        cursor.execute(query)
    cursor.close()
    conn.close()

def buscarAlumno(nombre):
    conn = db.connect("mibase.db")
    cursor = conn.cursor()
    rows = cursor.execute(f"SELECT * FROM alumnos WHERE nombre = '{nombre}';")
    rows = rows.fetchall()
    if(len(rows) == 0):
        print("No se ha encontrado ningún alumno con ese nombre")
    else:
        print("\nSe han encontrado los siguientes alumnos con ese nombre: ")
        for id,nom,ape in rows:
            print(f"Legajo: {id} - {nom} {ape}")
    cursor.close()
    conn.close()

def mostrarAlumnos():
    conn = db.connect("mibase.db")
    cursor = conn.cursor()
    rows = cursor.execute(f"SELECT * FROM alumnos;")
    rows = rows.fetchall()
    if(len(rows) == 0):
        print("No hay alumnos cargados en la base de datos")
    else:
        print("\nAlumnos cargados en la base de datos: ")
        for id,nom,ape in rows:
            print(f"Legajo: {id} - {nom} {ape}")
    cursor.close()
    conn.close()

arregloAlumnos = [[1,"Juan","Yofret"], [2,"Exequiel", "Sayago"], [3,"Santiago", "Perez"], [4,"Lucila", "Sosa"], [5,"Stella", "Mercado"], [6, "Isabel", "Casco"], [7, "Roberto", "Carlos"], [8, "Cristiano", "Ronaldo"], [9, "Juan", "Rodriz"]]

crearTabla("alumnos")
cargarRegistros(arregloAlumnos)
buscarAlumno("EliaXn")
buscarAlumno("Juan")
mostrarAlumnos()
