'''
Code made by: @genarobaarr
25 september 2024

Instruction: "Write a program where you have a list and then remove
repeted items, finally show the list."
"Escriba un programa donde tenga una lista y que, a continuación,
elimine los elementos repetidos, por último mostrar la lista."

'''

#Declaración de la lista 'lista'
    #Se le introducen valores a 'lista'
lista = [1, 2, 3, "Alex", 2, 2, 1, "Alex", 3]

#Proceso para quitar elementos repetidos
#Opción 1
'''
#Conversión de lista a conjunto para quitar elementos repetidos

    #Se convierte de una lista a un conjunto y se almacena en 'conjunto'
conjunto = set(lista)

    #Se devuelven los valores del conjunto a la lista
lista = list(conjunto)
'''

#Opción 2

#Simplificación de la Opción 1
lista = list(set(lista))

#Mostrando el resultado
print(lista)