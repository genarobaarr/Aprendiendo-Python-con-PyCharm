'''
Code made by: @genarobaarr
19 september 2024

Instruction: "Make a program that simulates an ATM with an initial
balance of $1000 and will have the following menu options:"
"Hacer un programa que simule un cajero automático con un saldo incial
de $1000 y tendrá el siguiente menú de opciones:"

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir

'''

#Declaración de variable 'opera' por parte del usuario
opera = int(input("Introduce la operación que quieres realizar"
             "\n1. Ingresar dinero en la cuenta"
             "\n2. Retirar dinero de la cuenta"
             "\n3. Mostrar dinero disponible"
             "\n4. Salir"
             "\n - > "))

#Declaración de variable 'saldo'
saldo = 1000

#Realizando comprobaciones con condicionales
if opera == 1: #Caso 1, depositar dinero
    ingreso = float(input("\nIntroduce el monto de dinero a ingresar: "))
    saldo += ingreso
    print("Depósito realizado con éxito")
    print(f"Tu saldo actual es de ${saldo}.")
elif opera == 2: #Caso 2, retiro de dinero
    retiro = float(input("\nIntroduce el monto de dinero a retirar: "))
    if retiro > saldo: #Caso 2.1 si el monto a retirar es mayor que el saldo
        print("El monto que quieres retirar es mayor a tu saldo actual.")
    else: #Caso 2.2 si el monto a retirar es menor que el saldo
        saldo -= retiro
        print("Retiro realizado con éxito")
        print(f"Tu saldo actual es de ${saldo}.")
elif opera == 3: #Caso 3, consultar saldo
    print(f"Tu saldo actual es de ${saldo}.")
elif opera == 4:#Caso 4, salir del programa
    print("Saliendo del programa")
else: #Si se ingresa una opción inválida
    print("Introduce uma opción válida")