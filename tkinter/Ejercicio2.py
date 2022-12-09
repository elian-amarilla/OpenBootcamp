import sys
import tkinter

window = tkinter.Tk()

def actualizar():
        if len(listbox.curselection())!=0:
            elegidos=''
            for posicion in listbox.curselection():
                elegidos+=listbox.get(posicion)+"\n"
            label2.configure(text=f"Usted seleccionó: \n{elegidos}", bg="black", fg="white")

lista = ["Python", "Java", "Javascript", "PHP", "Perl", "Ruby"]

label = tkinter.Label(window, text="Seleccione los lenguajes de programación que conoce: ")
label.pack()

lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items, selectmode=tkinter.MULTIPLE)
listbox.pack()

boton = tkinter.Button(text="Aceptar", command=actualizar)
boton.pack()

label2 = tkinter.Label(window, text="No seleccionó ningún lenguaje.")
label2.pack()

window.mainloop()
sys.exit(0)
