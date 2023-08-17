import random
def generar_enteros_aleatorios(x):
    numeros_generados=[random.randint(0,100) for _ in range(x) ]
    return numeros_generados
def mostrar_lista(lista_generada):
    print('La lista de números enteros aleatorios generada es:\n{}'.format(lista_generada))

def ordenar_lista(lista_generada):
    lista_ordenada=sorted(lista_generada)
    print('La lista ordenada de números enteros aleatorios es:\n{}'.format(lista_ordenada))
