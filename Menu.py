
from Calculadora import numero_de_cartas_validas

class menu():
    def __init__(self): 
        while True:
                x=input('''
        1. Iniciar programa
        2. Salir
        Escoja una opcion:''')
                if x =="1":
                    a=numero_de_cartas_validas()
                elif x =="2":
                    print("saliendo...")
                    break
                else:
                    print("Escoja un dato valido porfavor:")


a=menu()