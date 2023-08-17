"""Práctica 3""" 
def ingreso_numero_entero(x):
    try:
        numero=int(x)
        return numero
    except ValueError:
        print('{} no es un número entero'.format(x))
        return None

def main():
    lista_calificaciones=input('Ingrese una lista de calificaciones separadas por comas: ')
    lista_cadena=lista_calificaciones.split(',')
    lista=[]

    for calificacion_cadena in lista_cadena:
       try:
           calificacion=int(calificacion_cadena.strip())
           lista.append(calificacion)
       except ValueError:
           print('Error: {} no es una calificación'.format(calificacion_cadena.strip()))
    if lista:
        promedio=sum(lista)/len(lista)
        print('Las calificaciones son: {}'.format(lista))
        print('El promedio es: {}'.format(promedio))
    else:
        print('No se ingresaron datos válidos')

class CIRCULO:
    def __init__(self,radio):
        self.radio=radio
    def calculo_area(self):
        area=3.1416*self.radio**2
        return area

class RECTANGULO:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
    def calculo_area_rectangulo(self):
        area_rectangulo=self.largo*self.ancho
        return area_rectangulo

class Alumno:
    def __init__(self,nombre,numero_registro):
        self.nombre=nombre
        self.numero_registro=numero_registro
        self.edad=None
        self.notas=[]
    
    def display(self):
        print('Información del estudiante')
        print('Nombre:{}\nNúmero de registro: {}'.format(self.nombre,self.numero_registro))
        print('La edad del alumno es {}'.format(self.edad))
        print('Notas:')
        for i,nota in enumerate(self.notas,start=1):
            print('Nota {}:{}'.format(i,nota))
    def setAge(self,edad):
        self.edad=edad
    def setNota(self,notas):
        self.notas=notas

import mi_modulo
def main2():
    numeros_aleatorios=mi_modulo.generar_enteros_aleatorios(20)
    mi_modulo.mostrar_lista(numeros_aleatorios)
    mi_modulo.ordenar_lista(numeros_aleatorios)

import operaciones
def main3():
    ingreso_1=input('Ingrese el primer número: ')
    ingreso_2=input('Ingrese el segundo número: ')
    operaciones.funcion_suma(ingreso_1,ingreso_2)
    operaciones.funcion_resta(ingreso_1,ingreso_2)
    operaciones.funcion_producto(ingreso_1,ingreso_2)
    operaciones.funcion_division(ingreso_1,ingreso_2)

import math
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def cuadrante(self):
        if self.x==0 and self.y==0:
            return 'Está en el origen'
        elif self.y==0:
            return 'Está sobre el eje x'
        elif self.x==0:
            return 'Está sobre el eje y'
        elif self.x>0 and self.y>0:
            return 'Está en el primer cuadrante'
        elif self.x<0 and self.y>0:
            return 'Está en el segundo cuadrante'
        elif self.x<0 and self.y<0:
            return 'Está en el tercer cuadrante'
        elif self.x>0 and self.y<0:
            return 'Está en el cuarto cuadrante'
    def vector(self,punto):
        vector_resultante=(punto.x-self.x,punto.y-self.y)
        return vector_resultante
    def distancia(self,punto):
        distancia_puntos=math.sqrt((punto.x-self.x)**2 + (punto.y-self.y)**2)
        return distancia_puntos

#Ejercicio 1:
print('____EJERCICIO 1____')
while True:
    numeros_ingresados=input('Ingrese dos numeros enteros en formato X/Y: ')
    n1,n2=numeros_ingresados.split("/")
    ingreso_numero_entero(n1)
    ingreso_numero_entero(n2)
    n1>=n2 and n2!=0
    try:
        n3=int(n1)/int(n2)*100
        if n3<1:
            print('E')
            break
        elif n3>99:
            print('F')
            break
        else:
            print('El resultado es {}%'.format(int(n3)))
            break
    except ValueError:
        print('Error de cálculo')
    except ZeroDivisionError:
        print('Error por división entre cero (0)')

#Ejercicio 2:
print('____EJERCICIO 2____')   
main()

#Ejercicio 3:
print('____EJERCICIO 3____') 
radio_ingresado=int(input('Ingrese el radio del circulo: '))
area_circulo=CIRCULO(radio_ingresado).calculo_area()
print('El área del circulo con radio {} es {}'.format(radio_ingresado,area_circulo))

#Ejercicio 4
print('____EJERCICIO 4____') 
largo_ingresado=int(input('Ingrese el largo del rectangulo: '))
ancho_ingresado=int(input('Ingrese el ancho del rectangulo: '))
area_rectangulo=RECTANGULO(largo_ingresado,ancho_ingresado).calculo_area_rectangulo()
print('El área del rectangulo con largo {} y ancho {} es {}'.format(largo_ingresado,ancho_ingresado,area_rectangulo))

#Ejercicio 5
print('____EJERCICIO 5____') 
nombre_ingresado=input('Ingrese el nombre del alumno: ')
numero_ingresado=input('Ingrese el número de registro del alumno: ')
datos_alumno=Alumno(nombre_ingresado,numero_ingresado)
edad_ingresada=int(input('Ingrese la edad del alumno: '))
datos_alumno.setAge(edad_ingresada)
numero_notas=int(input('¿Cuántas notas desea ingresas?: '))
notas_alumno=[]
for i in range(numero_notas):
    nota=float(input('Ingrese la nota del alumno: '))
    notas_alumno.append(nota)
datos_alumno.setNota(notas_alumno)

datos_alumno.display()

#Ejercicio 6
print('____EJERCICIO 6____') 
punto_ingreso_1=input('Ingrese los números del primer punto separado por comas: ')
punto_ingreso_2=input('Ingrese los números del segundo punto separado por comas: ')
num1,num2=punto_ingreso_1.split(',')
num3,num4=punto_ingreso_2.split(',')
punto1=Punto(int(num1),int(num2))
punto2=Punto(int(num3),int(num4))
print('Punto 1: ',(int(num1),int(num2)))
print('Punto 2: ',(int(num3),int(num4)))
print('Cuadrante del punto 1: ', Punto(int(num1),int(num2)).cuadrante())
print('Cuadrante del punto 2: ', Punto(int(num3),int(num4)).cuadrante())
print('Vector entre el punto 1 y punto 2: ', punto1.vector(punto2))
print('Distancia entre el punto 1 y punto 2: ', punto1.distancia(punto2))
#Ejercicio 7
print('____EJERCICIO 7____')
main2()

#Ejercicio 8
print('____EJERCICIO 8____')
main3()

