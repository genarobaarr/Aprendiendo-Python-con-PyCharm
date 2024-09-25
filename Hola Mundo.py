# Este es mi primer programa en Python
'''
    Probando los comentarios multilíena
'''

'''
Probando el print y tipos de datos
'''

#Hola Mundo
print("Hola Mundo")

#Comenzando a probar los tipos de datos
numero = 7
cadena = 'Esta es una cadena "medio tarada"'
valor = False
#Imprimo los valores y sus tipos de dato
print(numero)
print("El tipo de dato es: ", type(numero), "\n")

print(cadena)
print("El tipo de dato es: ", type(cadena), "\n")

print(valor)
print("El tipo de dato es: ", type(valor), "\n")

'''
Probando Operadores aritméticos
'''

num1 = 10
num2 = 6.7
suma = (num1 + num2) * 10 / 6
print("El resultado es:", suma)
print(type(suma), "\n")

#Probando el redondeo
num3 = 15
num4 = 4

resultado =  num3 / num4
print("El resultado sin redondear es:", resultado)
resultado = num3 // num4
print("El resultado redondeado es:", resultado, "\n")

#Probando el módulo
num3 = 10
num4 = 3
resultado =  num3 % num4
print("El resultado módulo es:", resultado, "\n")

#Probando exponentes
num3 = 2
num4 = 5
resultado =  num3 ** num4
print("El resultado de 2 a la 5ta es:", resultado, "\n")

#Expresiones matematicas
resultado = 3**3 * ((13/5)-(2*4))
string = "3**3 * ((13/5)-(2*4))"
print("El resultado de ", str, " es: ", resultado, "\n")

'''
Operadores Relacionales
'''

#Menor que <

resultado = 10 < 20
print("Es 10 < 20?", resultado)
#Menor o igual que <

resultado = 10 <= 20
print("Es 10 <= 20?", resultado)

#Mayor que >

resultado = 10 > 20
print("Es 10 > 20?", resultado)
#Mayor o igual que >

resultado = 10 >= 20
print("Es 10 >= 20?", resultado)

#Igualdad ==

resultado = 10 == 20
print("Es 10 == 20?", resultado)

#Diferencia !=

resultado = 10 != 20
print("Es 10 != 20?", resultado, "\n")

'''
Combinación de Operadores aritméticos con Operadores relacionales
'''

a = 10
b = 20
c = 30
resultado = a + b != c
print("Es 10 + 20 != que 30? ", resultado, "\n")

'''
Operadores lógicos
'''

a = 10
b = 12
c = 13
d = 10

#Realizando una expresion con operadores lógicos y relacionales
resultado = ((a > b) or (a < c) and (a == c) or (a >= b))
print("El resultado de ((a>b) or (a<c) and (a==c) or (a >= b)) es: ", resultado, "\n")

#Más ejemplos
a = 10
b = 15
c = 20
resultado = ((a < b) and (b < c))
print("El resultado de ((a<b) and (b<c)) es:", resultado)
resultado = ((a > b) and (b < c))
print("El resultado de ((a>b) and (b<c)) es:", resultado)
resultado = ((a > b) or (b < c))
print("El resultado de ((a>b) and (b<c)) es:", resultado)
resultado = not((a > b) or (b < c))
print("El resultado de not((a>b) and (b<c)) es:", resultado, "\n")

'''
Prioridades de todos los Operadores:
1. ()
2. **
3. *, /, %, not
4. +, -, and
5. >, <, ==, >=, <=, !=, or
'''

'''
Operadores de asignación
'''

a = 0
#Suma en asignación
a += 5
print("El resultado de a += 5 es:", a)

#Resta en asignación
a -= 2
print("El resultado de a -= 2 es:", a)

#Multiplicación en asignación
a *= 3
print("El resultado de a *= 3 es:", a)

#División en asignación
a /= 3
print("El resultado de a /= 3 es:", a)

#Potencia en asignación
a **= 2
print("El resultado de a **= 2 es:", a)

#Módulo en asignación
a %= 2
print("El resultado de a %= 2 es:", a, "\n")

'''
Salidas de datos
'''

nombre = "Alex"
edad = 45
#Estas son 3 maneras de mostrar mensajes en la consola
print("Hola", nombre, "tienes", edad, "años.")
print("Hola {} tienes {} años.".format(nombre,edad))
print(f"Hola {nombre} tienes {edad} años.\n")

'''
Entrada de datos
'''
#Lo comento para no interferir con las siguientes cosas
'''
#Implementando el primer input de una cadena
nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre}!")

#Implementando el primer input de un entero
numero = int(input("Escribe un número: "))
print(f"Tu número es: {numero+1}!")

#Implementando el primer input de un entero
numero = float(input("Escribe un número: "))
print(f"Tu numero float es: {numero+1.12}!\n")
'''

'''
Funciones integradas
'''

#Pasar de tipos de datos a otros

#De cadena a int
n = int("11")
print(f"{n} es: ",type(n))

#De cadena a float
n = float("11.865")
print(f"{n} es: ",type(n))

#De float a cadena
n = str(10.98)
print(f"{n} es: ",type(n))

#De int a bin (binario)
n = bin(10)
print(f"{n} es: ",type(n))

#De int a hex (hexadecimal)
n = hex(10)
print(f"{n} es: ",type(n))

#De bin a int
n = int("0b1010",2)
print(f"{n} es: ",type(n))

#De bin a int
n = int("0xa",16)
print(f"{n} es: ",type(n),"\n")

#Sacar valor absoluto de un número
n = abs(-8)
print(f"Sacar valor absoluto de un número: {n}")

#Redondear un número
n = round(5.6)
print(f"Redondear un número: {n}")
n = round(5.4)
print(f"Redondear un número: {n}")

#Saber la longitud de una cadena
n = len("Genaro y Alex son amigos")
print(f"Saber la longitud de una cadena: {n}\n")

'''
Condicionales if - elif - else
'''

#if - elif - else
num1 = 5
if num1 < 0:
    print(f"El numero {num1} es negativo")
elif num1 == 0:
    print(f"El numero {num1} es cero")
else:
    print(f"El numero {num1} es positivo")
print("\n")

#Condicionales combinados
edad = 18
#1
if edad > 0 and edad < 100:
    print("Bien!")
    if edad >= 18:
        print("Es mayor de edad!")
    else:
        print("Es menor de edad!")
else:
    print("Coloca una edad correcta")
#2
if 0 < edad < 100:
    print("Bien!")
    if edad >= 18:
        print("Es mayor de edad!")
    else:
        print("Es menor de edad!")
else:
    print("Coloca una edad correcta")
print("\n")

'''
Colecciones
'''
'''
Listas
'''

listaParaEjemplo = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 10.567, [1, 2, 3], True]

print(listaParaEjemplo[2])
print(listaParaEjemplo[-3])
print(listaParaEjemplo[1:3])
print(listaParaEjemplo[:3])
print(listaParaEjemplo[3:])
print("\n")

#Saber la longitud (cantidad de elementos de una lista)
print(len(listaParaEjemplo))
print("\n")

#Agregar elementos al final de la lista
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)
lista1.append("Good job!")
print(lista1)
print("\n")

#Agregar elementos en una posición determinada
lista1.insert(2, 2.5)
print(lista1)
print("\n")

#Agregar varios elementos a la vez al final de la lista
lista1.extend([7, 8, 9])
print(lista1)
print("\n")

#Sumar dos listas
lista2 = [10,11,12,13]
listaSuma = lista1 + lista2
print(listaSuma)
print("\n")

#Saber si un elemento se encuentra el valor buscado
print(2.5 in lista1)
print("Good job!" in lista1)
print(15 in lista1)
print("\n")

#Saber en que indice se encuetra el valor buscado
print(lista1.index(2))
print(lista1.index("Good job!"))
print("\n")

#Saber cuantos valores del elemento buscado existen
lista1.extend([7, 8, 9, 1, 2.5, "Good job!", 8, 1]) #Agregando valores para ver el ejemplo
print(lista1.count(1))
print(lista1.count("Good job!"))
print(lista1.count("Bad job!"))
print("\n")

#Eliminar un elemento de la lista
lista3 = [1, 2, 3, 4, 5, "Hello!"]
lista3.pop() #Se elimina el ultimo elemento de la lista
print(lista3)
lista3.pop(3) #Se elimina elemento del indice
print(lista3)
print("\n")

#Eliminar un elemento de la lista si no se el indice
lista3.remove(1)
print(lista3)
lista3.remove(2)
print(lista3)
print("\n")

#Eliminar toda la lista completa
lista3.clear()
print(lista3)
print("\n")

#Como invertir una lista
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista4.reverse()
print(lista4)
print("\n")

#Hacer que en una lista se guarden dichas veces los elementos
    #lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
lista4 = lista4 * 2
print(lista4)
print("\n")

#Ordenar todos los elementos de la lista ascendentemente
lista5 = [5, 7, -1, 2, -6, 3, 9, 4, 8, 10, 6, 1]
lista5.sort()
print(lista5)
print("\n")

#Ordenar todos los elementos de la lista descendentemente
lista6 = [5, 7, -1, 2, -6, 3, 9, 4, 8, 10, 6, 1]
lista6.sort(reverse=True)
print(lista6)
print("\n")

'''
Tuplas
'''
tupla = (4, "Hello!", 6.78, [1, 2, 3], 4, 5)
print(tupla)
print(tupla[1])
print(tupla[-1])
print(tupla[2:])
print(4 in tupla) #Saber si un elemento se encuentra en la tupla
print(tupla.index("Hello!")) #Saber en que indice se encuetra el valor buscado
print(tupla.count(4)) #Saber cuantos valores del elemento buscado existen
print(len(tupla)) #Saber la longitud (cantidad de elementos de una tupla)
print("\n")

#Transformar una tupla a una lista
listaDesdeTupla = list(tupla)
print(listaDesdeTupla)
print("\n")

#Transformar de una lista a una tupla
tuplaDesdeLista = tuple(lista4)
print(tuplaDesdeLista)
print("\n")

'''
Conjuntos
'''
conjunto = set()
conjunto = {1, 2, 3, "Good job!", 4.56, 1, 2, 3}
print(conjunto)
print("\n")

#Agregar elementos a un conjunto
conjunto.add(5)
conjunto.add("Bad job!")
conjunto.add('z')
print(conjunto)
print("\n")

#Como saber si un elemento existe en el conjunto
print(3 in conjunto)
print(4.56 in conjunto)
print(6 in conjunto)
print(6 not in conjunto)
print("\n")

#Eliminar un elemento de un conjutno
conjunto.discard(3)
conjunto.discard("Good job!")
print(conjunto)
print("\n")

#Como vaciar un conjunto
conjunto.clear()
print(conjunto)
print("\n")

#Calcular si un conjunto es igual a otro
conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5}
conjuntoC = {3, 2, 1}
print(conjuntoA == conjuntoB)
print(conjuntoB == conjuntoC)
print(conjuntoC == conjuntoA)
print("\n")

#Unir dos conjuntos (todos los elementos de los dos conjuntos)
conjuntoD = conjuntoA | conjuntoB
print(conjuntoD)
conjuntoD = conjuntoA | conjuntoC
print(conjuntoD)
print("\n")

#Intersección de dos conjuntos (elementos que están en los dos conjuntos)
conjuntoD = conjuntoA & conjuntoB
print(conjuntoD)
conjuntoD = conjuntoA & conjuntoC
print(conjuntoD)
print("\n")

#Diferencia de dos conjuntos (todos los elementos de A que no están en B)
conjuntoD = conjuntoA - conjuntoB
print(conjuntoD)
conjuntoD = conjuntoA - conjuntoC
print(conjuntoD)
print("\n")

#Diferencia SIMETRICA de dos conjuntos (todos los elementos que no se repiten en ambos conjuntos)
conjuntoD = conjuntoA ^ conjuntoB
print(conjuntoD)
conjuntoD = conjuntoA ^ conjuntoC
print(conjuntoD)
print("\n")

#Saber si un conjunto es un subconjunto de otro conjunto
conjuntoD = {1, 2, 3, 4, 6}
print(conjuntoA.issubset(conjuntoD))
print(conjuntoB.issubset(conjuntoD))
print(conjuntoC.issubset(conjuntoD))
print("\n")

#Saber si un conjunto es un superconjunto de otro conjunto
print(conjuntoD.issuperset(conjuntoA))
print(conjuntoD.issuperset(conjuntoB))
print(conjuntoD.issuperset(conjuntoC))
print("\n")

#Saber si dos conjuntos son disconexos (no tener ningún elemento en común)
print(conjuntoA.isdisjoint(conjuntoB))
print(conjuntoB.isdisjoint(conjuntoC))
print(conjuntoC.isdisjoint(conjuntoA))
print("\n")

#Como hacer un conjunto inmutable
conjuntoE = frozenset({1, 2, 4, 8, 3, 6, 9})

'''
Diccionarios
'''
# Creación de diccionario
diccionarioEjemplo = {"azul" : "bleu", "rojo" : "red", "verde" : "green"}
print(diccionarioEjemplo)
print(diccionarioEjemplo["azul"])
print(diccionarioEjemplo["rojo"])
print("\n")

#Agregar nuevos elementos al diccionario
diccionarioEjemplo["amarillo"] = "yellow"
print(diccionarioEjemplo)

#Modificar un elemento del diccionario
diccionarioEjemplo["azul"] = "blue"
print(diccionarioEjemplo)

#Eliminar un elemento del diccionario
del(diccionarioEjemplo["rojo"])
print(diccionarioEjemplo)
print("\n")

#Ejemplos más complejo
#1
diccionario = {"Alejandro" : {"edad" : 20, "estatura" : 1.65}, "Jose" : {"edad" : 23, "estatura" : 1.77}, "Maria" : {"edad" : 19, "estatura" : 1.57}}
print(diccionario["Alejandro"])
print("\n")

#2
equipo = {10 : "Paulo Dybala", 11 : "Douglas Costa", 7 : "Cristiano Ronaldo", 17 : "Mario Mandzukic"}
print(equipo)
print(equipo[10])
print(equipo[7])
print("\n")

#Saber la longitud del diccionario (cantidad de elementos hay)
print(len(equipo))
print("\n")

#Saber si una clave existe
print(17 in equipo)
print(6 in equipo)

#Que hacer si una clave no existe y evitamos excepción en consola
print(equipo.get(6, "No existe un jugador con ese dorsal"))
print("\n")

#Mostrar solo las claves del diccionario
print(equipo.keys())

#Mostrar solo los valores del diccionario
print(equipo.values())
print("\n")

#Eliminar todos los elementos del diccionario
equipo.clear()
print(equipo)
print("\n")

'''
Pilas
'''

pila = [1, 2, 3]
print(pila)

#Agregar elemento por el final de la pila
pila.append(4)
pila.append(5)
print(pila)

#Sacar elemento por el final de la pila
x = pila.pop()
print(f"Sacando el elemento {x}")
print(pila)
print("\n")

'''
Colas
'''

cola = ["Maria", "Alejandro", "Jose", "Mario"]
print(cola)

#Agregar elemento por el final de la cola
cola.append("Karla")
cola.append("Flor")
print(cola)

#Sacar elemento por el inicio de la cola
x = cola.pop(0)
print(f"Atendiendo ahora a {x}")
print(cola)
print("\n")