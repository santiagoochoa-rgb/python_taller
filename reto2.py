nombre = input("Nombre del cliente: ")
comida = float(input("Valor de la comida: "))
bebidas = float(input("Valor de las bebidas: "))

subtotal = comida + bebidas
propina = subtotal * 0.10
total = subtotal + propina

print("Cliente:", nombre)
print("Subtotal:", subtotal)
print("Propina:", propina)
print("Total a pagar:", total)
