"""Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100."""
import random

randomNumbers = []
randomNum = 0
for i in range(0, 10):
    randomNum = random.randint(0, 101)
    randomNumbers.append(randomNum)
print(randomNumbers)