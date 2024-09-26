'''
Code made by: @genarobaarr
25 september 2024

Instruction: "Write a program that creates a list with the following
characters of The Lord of the Rings:"
"Escriba un programa donde cree una lista con los siguientes personajes
de El Señor de los Anillos"

'''

#Creación de la lista 'personajes'
personajes = []

#Declaración de el diccionario 'individualPerson'

#Se establecen nombres, clases y razas
individualPerson = {"Nombre" : "Aragorn", "Clase" : "Guerrero", "Raza" : "Dúnadan del Norte"}
#Se pasa el personaje a la lista 'personajes'
personajes.append(individualPerson)

#Se establecen nombres, clases y razas
individualPerson = {"Nombre" : "Gandalf",  "Clase" : "Mago", "Raza" : "Istar"}
#Se pasa el personaje a la lista 'personajes'
personajes.append(individualPerson)

#Se establecen nombres, clases y razas
individualPerson = {"Nombre" : "Legolas", "Clase" : "Arquero", "Raza" : "Elfo Sindar"}
#Se pasa el personaje a la lista 'personajes'
personajes.append(individualPerson)

#Mostrar la lista resultante
print(personajes)

