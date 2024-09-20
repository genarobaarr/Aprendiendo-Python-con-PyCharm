'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Make a program that asks for 2 numbers and finds out which
of them is even or if both are"
"Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par,
o si ambos lo son"

'''

#Declaración de variables 'a', 'b' por parte del usuario
a = int(input("Introduce el primer número - > "))
b = int(input("Introduce el segundo número - > "))

#Realizando comprobaciones con condicionales e imprimiendo respuesta
if a % 2 == 0 and b % 2 == 0:
    print(f"Los números {a} y {b} son pares.")
elif a % 2 == 0 and b % 2 != 0:
    print(f"El número {a} es par y {b} es impar.")
elif a % 2 != 0 and b % 2 == 0:
    print(f"El número {b} es par y {a} es impar.")
else:
    print(f"Los números {a} y {b} no son pares.")