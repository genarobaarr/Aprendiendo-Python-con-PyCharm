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
resultado = ((a>b) or (a<c) and (a==c) or (a >= b))
print("El resultado de ((a>b) or (a<c) and (a==c) or (a >= b)) es: ", resultado, "\n")

#Más ejemplos
a = 10
b = 15
c = 20
resultado = ((a<b) and (b<c))
print("El resultado de ((a<b) and (b<c)) es:", resultado)
resultado = ((a>b) and (b<c))
print("El resultado de ((a>b) and (b<c)) es:", resultado)
resultado = ((a>b) or (b<c))
print("El resultado de ((a>b) and (b<c)) es:", resultado)
resultado = not((a>b) or (b<c))
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