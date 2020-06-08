#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un calculadora, se ingresará por línea de comando dos números reales
    y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
    
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print('Ingrese el primer número real a operar:')

    numero_1 = int(input()) 

    print('Ingrese el segundo numero real para operar:')

    numero_2 = int(input())

    suma = numero_1 + numero_2

    resta = numero_1 - numero_2 

    multiplicacion = numero_1 * numero_2

    division = numero_1 / numero_2
   # Suma
    print('El resultado de sumar' ,numero_1, 'y' ,numero_2, 'es',suma)
    # Resta
    print('El resultado de restar',numero_1,'y',numero_2,'es',resta)
    # División
    print('El resultado dividir',numero_1,'y',numero_2,'es',division)
    # Multiplicación
    print('El resultado multiplicar',numero_1,'y',numero_2,'es',multiplicacion)

def ej2():
    # Ejercicios de práctica numérica y cadenas
    
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea entienda de que se
      está hablando.

    '''
    print('Ingrese su nombre/s y apellido/s:')
    nombre = str(input())

    print('Ingrese su D.N.I (sin puntos):')
    DNI = int(input())

    print('Ingrese su edad:')
    Edad = int(input())

    print('Ingrese su altura:')
    Altura = float(input())

    print("Nombre completo:",nombre, "D.N.I:",DNI )

    print("Nombre completo:", nombre, "Edad:",Edad, "Altura:",Altura)


def ej3():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar el método "split"
    Mostraremos un ejemplo:
    
    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
        
    '''
    print("Ingrese nombre/s y apellido/s del padre")
    padre_1 = str(input())
    

    print("Ingrese nombre/s y apellido/s de la madre")
    padre_2 = str(input())

    print( "Ingrese nombre/s de su hijo")
    hijo = str(input())

    print(padre1lista)

    padre2lista = padre_2.split()

    #print(padre2lista)

    apellido_padre = padre1lista [2]

    #print(apellido_padre)

    apellido_madre = padre2lista [2]

    #print(apellido_madre)

    print(hijo, apellido_padre, apellido_madre)

def ej4():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine si una persona_2 es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir, primero el nombre y luego
    el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido en el nombre completo
      de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    
        
    '''

    print('Ingrese por favor el primer nombre y el apellido de la primera persona')
    persona_1 = str(input())

    print('Ingrese por favor el primer nombre y el apellido de la segunda persona')
    persona_2 = str(input())

    persona1_lista = persona_1.split()

    persona2_lista = persona_2.split()

    apellido_1 = persona1_lista [1]

    apellido_2 = persona2_lista [1]

    parientes_1 = persona2_lista [1] in persona1_lista

    if parientes_1:
       print('Las personas son parientes')
    else:
       print('las personas no son parientes')


def ej5():
    # Ejercicios de práctica con cadenas
       
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos un el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    

    '''
    print('Ingrese su nombre completo')

    nombre_completo = str(input())

    print(nombre_completo.lower())

    print(nombre_completo.upper())

    print(nombre_completo.capitalize())

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
