'''
Code made by: @genarobaarr
18 september 2024

Instruction: "Make a program to introduce the radius of a circle and
report back its area and the length of its circumference"
"Hacer un programa para ingresar el radio de un círculo y se reporte su
área y la longitud de su circunferencia"

        area = π * r^2
        length = 2 * π * r
'''

#Opcion 1
'''
#Declaración de variable 'π'
pi = 3.14159265359
#Declaración de variable 'r' por parte del usuario
r = float(input("Introduce el valor del radio de tu ciculo - > "))

#Calculo del área:
area = pi * r**2

#Impresión del resultado del área:
print(f"\nEl área de tu círculo es: {area}\n")

#Calculo de la longitud de la circunferencia
circ = 2 * pi * r

#Impresión del resultado de la longitud de la circunferencia:
print(f"La longitud de la circunferencia de tu círculo es: {circ}")
'''

#Opcion 2
#Importa el módulo 'math'
import math

#Declaración de variable 'r' por parte del usuario
r = float(input("Introduce el valor del radio de tu ciculo - > "))

#Calculo del área:
area = math.pi * r**2

#Impresión del resultado del área:
print(f"\nEl área de tu círculo es: {area:.3f}\n")

#Calculo de la longitud de la circunferencia
circ = 2 * math.pi * r

#Impresión del resultado de la longitud de la circunferencia:
print(f"La longitud de la circunferencia de tu círculo es: {circ:.3f}")

#Se colocó :.3f para especificar que solo queremos que se
#muestren 3 decimales después del punto