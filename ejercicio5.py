# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def esBisiesto(anio):
    if(anio % 4 == 0):
        if(anio % 100 != 0 or (anio % 100 == 0 and anio % 400 == 0)):
            return True
    return False


valor = int(input("Ingrese el anio a evaluar: "))

if(esBisiesto(valor)):
    print("%d Es un anio bisiesto." %(valor))
else:
    print("%d No es un anio bisiesto." %(valor))

# Fuente: https://learn.microsoft.com/es-es/office/troubleshoot/excel/determine-a-leap-year
