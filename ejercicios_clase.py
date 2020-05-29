#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())
    
    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)

    print ( numero_1, numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    suma = numero_1 + numero_2

    resta = numero_1 - numero_2 

    multiplicacion = numero_1 * numero_2

    division = numero_1 / numero_2

    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    # Suma
    print('El resultado de sumar' ,numero_1, 'y' ,numero_2, 'es',suma)
    # Resta
    print('El resultado de restar',numero_1,'y',numero_2,'es',resta)
    # División
    print('El resultado dividir',numero_1,'y',numero_2,'es',division)
    # Multiplicación
    print('El resultado multiplicar',numero_1,'y',numero_2,'es',multiplicacion)
def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)
    print( numero_3, numero_4)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    
    suma = numero_3 + numero_4

    resta = numero_3 - numero_4 

    multiplicacion = numero_3 * numero_4

    division = numero_3 / numero_4

    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    print('El resultado de sumar' ,numero_3, 'y' ,numero_4, 'es',suma)
    # Resta
    print('El resultado de restar',numero_3,'y',numero_4,'es',resta)
    # División
    print('El resultado dividir',numero_3,'y',numero_4,'es',division)
    # Multiplicación
    print('El resultado multiplicar',numero_3,'y',numero_4,'es',multiplicacion)
    
def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    nombre_completo = (nombre + apellido)

    # Imprima su nombre completo

    print(nombre, apellido)

    # Imprimir la cantidad de letras que posee su nombre completo
    nombre_completo_len = len(nombre_completo)
    print(nombre_completo, 'tiene',nombre_completo_len,'caracteres')


def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    caracter_inicial_1 = palabra_1[0]
    caracter_inicial_2 = palabra_2[0]
    caracter_inicial_3 = palabra_3[0]

    print(caracter_inicial_1 + caracter_inicial_2 + caracter_inicial_3)

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    sub_text1_len = len(palabra_1)

    #print(sub_text1_len)

    sub_text2_len = len(palabra_2)

    #print(sub_text2_len)

    palabra_3 = palabra_1[:4]

    palabra_4 = palabra_2[1:sub_text2_len]

    print(palabra_3 + palabra_4)
    

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()

