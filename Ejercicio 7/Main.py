"""
Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario.
La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. (CRUD)
Crea un menú para las distintas opciones e implementa una función para cada opción.
"""

def list():
    print("1) Add contact")
    print("2) Delete contact")
    print("3) Search contact")
    print("0) Exit")

def add():
    code = len(contactList)
    name = input("Introduce name: ")
    phoneNumber = int(input("Introduce phone number: "))
    contact = (code, name, phoneNumber)
    contactList.append(contact)
    
def delete():
    code = int(input("Introduce the code of the contact you would like to delete: "))
    if code in contactList:
        for currentContact in contactList:
            if currentContact.code == code:
                contactList.remove(currentContact)
    else:
        print("The following contact does not exist.")

def search():
    name = input("Introduce the name of the contact that you are looking for: ")
    if name in contactList:
        for currentContact in contactList:
            if currentContact.name == name:
                print("Code:", currentContact.code)
                print("Name:", currentContact.name)
                print("Phone Number:", currentContact.phoneNumber)

contactList = []
print("Welcome!")
option = 1
while option != 0:
    list()
    try:
        option = int(input("Select one of the following options above: "))
    except:
        print("Make sure the following option is an integer number!")
    if option == 1:
        add()
    if option == 2:
        delete()
    if option == 3:
        search()
    if option == 0:
        print("Have a nice day!")