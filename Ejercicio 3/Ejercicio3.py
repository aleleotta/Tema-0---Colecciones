"""
Realiza un programa que pida 8 números enteros y los almacene en una lista.
A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.
"""
numbers = []
for i in range(1, 9):
    num = int(input("Introduce a number "+str(i)+": "))
    numbers.append(num)
for currentNum in numbers:
    if currentNum%2==1:
        checkEven = "Odd"
        print(currentNum, checkEven)
    if currentNum%2==0:
        checkEven = "Even"
        print(currentNum, checkEven)