'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Determine the logical solution to the following operation:"
"Determinar la solución lógica de la siguiente operación":

        ((3+5*8)<3 and ((-6*4)+2<2)) or (a>b)
                         --
                          3

'''

#Declaración de variables 'a', 'b' por parte del usuario
a = float(input("Escribe tu número 'a' - > "))
b = float(input("Escribe tu número 'b' - > "))

#Realización de la expresión lógica
#Se almacena el resultado en una variable 'resultado'
resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
print(f"El resultado de la expresión es: {resultado}.\n")