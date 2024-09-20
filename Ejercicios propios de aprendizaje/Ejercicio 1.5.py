'''
Code made by: @genarobaarr
18 september 2024

Instruction: "A store offers a 15% discount on the total purchase
and a customer wants to know how much he will finally pay for his purchase"
"Una tienda ofrece un descuento del 15% sobre el total de la compra y un
cliente desea saber cuánto pagar finalmente por su compra."

'''

#Declaración de variable 'precio' por parte del usuario
precio = float(input("Introduce el valor total de tu compra - > "))

#Calculo del descuento:
desc = precio * 0.15

#Impresión del resultado del descuento:
print(f"\nEl descuento de 15% que se te aplicará sobre ${precio} será de ${desc:.2f}\n")

#Calculo del precio final
precio -= desc

#Impresión del resultado del precio final:
print(f"Lo que deberás pagar finalmente será ${precio:.2f}")

#Se colocó :.2f para especificar que solo queremos que se
#muestren 2 decimales después del punto