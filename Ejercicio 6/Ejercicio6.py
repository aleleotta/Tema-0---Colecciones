"""
Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia
de cada palabra en el texto.
"""
text = input("Write a text: ")
collection = text.split()
word = input("Introduce the word you are looking for: ")
found = 0
for currentNum in collection:
    if currentNum == word:
        found = found + 1
if found > 0:
    print("The following word was found "+str(found)+" times.")
else
    print("The following word was not found within the text.")