import sys
import tkinter
import time
from tkinter import ttk

window = tkinter.Tk()

def limpiar(event):
    seleccion.set("none")
    label2.configure(text="No hay nada seleccionado", bg="white", fg="black")

def mostrarSeleccionado():
    valor = int(seleccion.get())
    if valor == 0:
        label2.configure(text="Usted es un varon", bg="blue", fg="white")
    if valor == 1:
        label2.configure(text="Usted es una mujer", bg="pink", fg="black")
    if valor == 2:
        label2.configure(text="Usted no es binario", bg="gray", fg="white")

window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=3)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)

label1 = tkinter.Label(window, text="Seleccione su sexo", bg="red")
label1.grid(column = 2, row=0)

seleccion = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Masculino", value="0", variable=seleccion, command=mostrarSeleccionado)
r2 = ttk.Radiobutton(window, text="Femenino", value="1", variable=seleccion, command=mostrarSeleccionado)
r3 = ttk.Radiobutton(window, text="No binario", value="2", variable=seleccion, command=mostrarSeleccionado)

label2 = tkinter.Label(window, text="No hay nada seleccionado", bg="white", fg="black")
label2.grid(column = 2, row=5)

r1.grid(column=2, row=1, pady=5, padx=5)
r2.grid(column=2, row=2, pady=5, padx=5)
r3.grid(column=2, row=3, pady=5, padx=5)

boton1 = tkinter.Button(window, text="Limpiar")
boton1.grid(column=3,row=5)
boton1.bind('<Button-1>', limpiar)

window.mainloop()
sys.exit(0)
