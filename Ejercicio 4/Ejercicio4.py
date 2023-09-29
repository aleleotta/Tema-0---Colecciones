"""Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor."""
numbers = []
for i in range(1,11):
    num = int(input("Introduce number "+str(i)+": "))
    numbers.append(num)
numbers.sort()
for currentNum in numbers:
    print(str(currentNum), end=" ")