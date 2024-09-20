'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Make a program that asks for 3 numbers and finds out
wich one of them is bigger"
"Hacer un programa que pida 3 números y determine cuál es el mayor"

'''

#Declaración de variables 'a', 'b', 'c' por parte del usuario
a = int(input("Introduce el primer número - > "))
b = int(input("Introduce el segundo número - > "))
c = int(input("Introduce el tercer número - > "))

#Realizando comprobaciones con condicionales e imprimiendo respuesta
if a >= b and a >= c:
    print(f"{a} es el número mayor.")
elif b >= a and b >= c:
    print(f"{b} es el número mayor.")
elif c >= a and c >= b:
    print(f"{c} es el número mayor.")
