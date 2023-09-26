"""
Crea un programa que pida diez números reales por teclado, los almacene en una lista,
y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.
"""
numbers = []
for i in range(0, 10):
    inputNum = int(input("Introduce number "+str(i)+": "))
    numbers.append(inputNum)
print(numbers)
for currentNum in numbers: