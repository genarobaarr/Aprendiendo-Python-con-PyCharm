'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Make a program that exchange the value of two variables"
"Hacer un programa para intercambiar el valor de dos variables"
For example: Por ejemplo:


        a = 10  ------>   a = 5
        b = 5   ------>   b = 10
'''

#Declaración de variables 'a', 'b' por parte del usuario
a = float(input("Escribe tu número 'a' - > "))
b = float(input("Escribe tu número 'b' - > "))

#Opcion 1
'''
#Realización del intercambio
#Se crear variable auxiliar 'aux'
aux = a

#Se intercambia el valor de 'b' a 'a' y viceversa
a = b
b = aux

#Impresión
print(f"\nEl valor actual de 'a' es: {a}.")
print(f"El valor actual de 'b' es: {b}.")
'''

#Opcion 2
#Realización del intercambio
#Se pone lo siguiente:
a, b = b ,a

#Impresión
print(f"\nEl valor actual de 'a' es: {a}.")
print(f"El valor actual de 'b' es: {b}.")