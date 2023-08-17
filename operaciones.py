def funcion_suma(x,y):
    try:
        numero1=int(x)
        numero2=int(y)
        suma_numeros=numero1+numero2
    except ValueError:
        print('Error: Tipo de dato no válido')
    return print('La suma de números es {}'.format(suma_numeros))

def funcion_resta(x,y):
    try:
        numero1=int(x)
        numero2=int(y)
        restar_numeros=numero1-numero2
    except ValueError:
        print('Error: Tipo de dato no válido')
    return print('La resta de números es {}'.format(restar_numeros))

def funcion_producto(x,y):
    try:
        numero1=int(x)
        numero2=int(y)
        producto_numeros=numero1*numero2
    except ValueError:
        print('Error: Tipo de dato no válido')
    return print('El producto de números es {}'.format(producto_numeros))


def funcion_division(x,y):
    try:
        numero1=int(x)
        numero2=int(y)
        division_numeros=numero1/numero2
    except ValueError:
        print('Error: Tipo de dato no válido')
    except ZeroDivisionError:
        print('Error: No es posible dividir entre cero')
    return print('La división de números es {}'.format(division_numeros))