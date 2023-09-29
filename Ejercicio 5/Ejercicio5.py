"""
Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10
(utiliza 1 + Math.random()*10).
Luego pedirá un valor N y mostrará cuántas veces aparece N. 
"""

import random

integers = []
for i in range(1,101):
    num = random.randint(1, 10)
    integers.append(num)
searchNumber = int(input("What number would you like to search within the collection?"))
foundNumbers = 0
for i in integers:
    if i == searchNumber:
        foundNumbers = foundNumbers + 1
print(integers)
print("The following number has been found "+str(foundNumbers)+" times.")