'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Write an expression in algorithmic form:"
"Escribir una expresión en forma algorítmica:"

        a^3 * (b^2 - 2ac)
        -----------------
                2b

'''

#Declaración de variables 'a', 'b', 'c' por parte del usuario
a = float(input("Escribe tu número 'a' - > "))
b = float(input("Escribe tu número 'b' - > "))
c = float(input("Escribe tu número 'c' - > "))

#Realización de la expresión algoritmica
#Se almacena el resultado en una variable 'resultado'
resultado = (a**3 * (b**2 - 2*a*c)) / (2*b)
print(f"El resultado de la expresión es: {resultado}.\n")