'''
Code made by: @genarobaarr
19 september 2024

Instruction: "Build a program that simulates the operation of a
calculator which can do the four basic arithmetic operations(addition,
subtraction, multiplication and division). The user must specify
the operation with the first character of the operation name:"
"Construir un programa que simule el funcionamiento de una calculadora
que puede  realizar las cuatro operaciones aritméticas básicas (suma,
resta, multiplicación y división). El usuario debe especificar la
operación con el primer carácter del nombre de la operacion:"

S, s - > suma
R, r -> resta
P, p, M, m -> multiplicación
D, d - > división

'''

#Declaración de variable 'char' por parte del usuario
char = input("Introduce la operación que quieres realizar"
             "\nS, s - > suma"
             "\nR, r - > resta"
             "\nP, p, M, m - > multiplicación"
             "\nD, d - > división"
             "\n - > ").upper()
#char = char.upper() #Otro modo de uso

#Declaración de variable 'n' con la longitud de 'char'
n = len(char)

#Realizando comprobaciones con condicionales
if n == 1:
    if char == "S": #Realiza la suma
        num1 = float(input("Introduce el número 1 a sumar: "))
        num2 = float(input("Introduce el número 2 a sumar: "))
        print(f"La suma de {num1} + {num2} es: {num1 + num2}")
    elif char == "R": #Realiza la resta
        num1 = float(input("Introduce el número 1 a restar: "))
        num2 = float(input("Introduce el número 2 a restar: "))
        print(f"La resta de {num1} - {num2} es: {num1 - num2}")
    elif char == "P" or char == "M": #Realiza la multiplicación
        num1 = float(input("Introduce el número 1 a multiplicar: "))
        num2 = float(input("Introduce el número 2 a multiplicar: "))
        print(f"La multiplicación de {num1} x {num2} es: {num1 * num2}")
    elif char == "D": #Realiza la división
        num1 = float(input("Introduce el número 1 a dividir: "))
        num2 = float(input("Introduce el número 2 a dividir: "))
        print(f"La división de {num1} / {num2} es: {num1 / num2}")
    else: #En caso de que se introduzca un caracter incorrecto
        print("Introduce un carácter correcto.")
else: #En caso de que se introduzca más de un caracter
    print("Introduce sólo un carácter.")