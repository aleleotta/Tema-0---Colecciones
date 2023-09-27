"""
Crea un programa que pida diez números reales por teclado, los almacene en una lista,
y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.
"""
numbers = []
for i in range(0, 10):
    inputNum = int(input("Introduce number "+str(i)+": "))
    numbers.append(inputNum)
print(numbers)
min = 0
max = 0
firstExec = 0
for currentNum in numbers:
    if firstExec == 0:
        min = currentNum
        firstExec = 1
    if currentNum > max:
        max = currentNum
    if currentNum < min:
        min = currentNum
print("Max: "+str(max))
print("Min: "+str(min))