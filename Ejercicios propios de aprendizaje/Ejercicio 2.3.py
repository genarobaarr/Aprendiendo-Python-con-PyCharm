'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Make a program that asks for a character and tells if its
a vowel or not"
"Hacer un programa que pida un carácter e indique si es una vocal  o no"

'''

#Declaración de variable 'a' por parte del usuario
a = input("Introduce tu carácter - > ").lower()
#a = a.lower() #Otro modo de uso

#Declaración de variable con la longitud de 'a'
n = len(a)

#Realizando comprobaciones con condicionales e imprimiendo respuesta
if n == 1:
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        print("Sí es una vocal.")
    else:
        print("No es una vocal.")
else:
    print("Introduce sólo un carácter.")