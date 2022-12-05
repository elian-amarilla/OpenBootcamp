# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter 
# y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

lista = [1,3,5,6,10,22,15,5,1]
resultado = reduce(lambda x,y: x+y, list(filter(lambda x: x%2 != 0, lista)))
print(f"El resultado de la suma de los impares de la lista da {resultado}")
