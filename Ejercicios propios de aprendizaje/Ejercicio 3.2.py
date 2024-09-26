'''
Code made by: @genarobaarr
25 september 2024

Instruction: "Write a program that has two lists and then creates
the following lists (in which there should be no repetitions):"
"Escriba un programa que tenga dos listas y que, a continuación, cree
las siguientes listas (en las que no debe haber repeticiones):"

Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Lista de palabras que aparecen en ambas listas.

'''

#Declaración de listas 'lista1' y 'lista2'
lista1 = ["James", "Patricia", "Michael", "Robert", "John", "William",
          "Anthony", "Jessica", "Linda", "Matthew", "Elizabeth", "Jacob"]
lista2 = ["Jack", "Elizabeth", "James", "Richard", "Linda", "Susan",
          "Thoams", "Patricia", "David", "Betty", "Sandra", "Steven"]



#Declaración de conjuntos 'conjunto1' y 'conjunto2'
#Se guardan en ambos conjuntos ambas listas
#Además aquí se eliminarían las repeticiones (si existieran)
conjunto1 = set(lista1)
conjunto2 = set(lista2)

#********************
#Lista de palabras que aparecen en las dos listas.
conjuntoUnion = conjunto1 | conjunto2

#Conversión del conjunto a lista
listaUnion = list(conjuntoUnion)

#Mostrando los resultados
print(f"\nLista de palabras que aparecen en las dos listas:"
      f"\n{listaUnion}")

#********************
#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
conjuntoDiferencia1 = conjunto1 - conjunto2

#Conversión del conjunto a lista
listaDiferencia1 = list(conjuntoDiferencia1)

#Mostrando los resultados
print(f"\nLista de palabras que aparecen en la primera lista, pero no en la segunda:"
      f"\n{listaDiferencia1}")

#********************
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
conjuntoDiferencia2 = conjunto2 - conjunto1

#Conversión del conjunto a lista
listaDiferencia2 = list(conjuntoDiferencia2)

#Mostrando los resultados
print(f"\nLista de palabras que aparecen en la segunda lista, pero no en la primera:"
      f"\n{listaDiferencia2}")

#********************
#Lista de palabras que aparecen en ambas listas.
conjuntoInterseccion = conjunto1 & conjunto2

#Conversión del conjunto a lista
listaInterseccion = list(conjuntoInterseccion)

#Mostrando los resultados
print(f"\nLista de palabras que aparecen en ambas listas:"
      f"\n{listaInterseccion}")