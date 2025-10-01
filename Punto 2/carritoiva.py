subtotal = 0
ordenes = {}

while True:
    print("Menú del Restaurante")
    print("1. Bandeja Paisa - $40,000")
    print("2. Sancocho de Gallina - $40,000")
    print("3. Churrasco - $50,000")
    print("4. Arroz con Pollo - $30,000")
    print("5. Empanadas - $15,000")
    print("6. Ensalada - $20,000")
    print("7. Arepa con Queso - $10,000")
    print("8. Salir")
    
    opcion = input("Ingrese el número de la opción que desea: ")
    
    if opcion == '8':
        break

    match opcion:
        case '1':
            plato = "Bandeja Paisa"
            precio = 40000
        case '2':
            plato = "Sancocho de Gallina"
            precio = 40000
        case '3':
            plato = "Churrasco"
            precio = 50000
        case '4':
            plato = "Arroz con Pollo"
            precio = 30000
        case '5':
            plato = "Empanadas"
            precio = 15000
        case '6':
            plato = "Ensalada"
            precio = 20000
        case '7':
            plato = "Arepa con Queso"
            precio = 10000
        case _:
            print("Opción no válida, intente de nuevo.\n")
            continue

    cantidad = int(input(f"Ingrese la cantidad de {plato}: "))
    while cantidad < 0:
        print("La cantidad no puede ser negativa. Intente nuevamente.")
        cantidad = int(input(f"Ingrese la cantidad de {plato}: "))
    
    subtotal += precio * cantidad
    if plato in ordenes:
        ordenes[plato] += cantidad
    else:
        ordenes[plato] = cantidad
    
    print()

respuesta = input("¿Desea agregar propina del 5%? (si/no): ").lower()
if respuesta == 'si':
    propina = subtotal * 0.05
else:
    propina = 0

iva = subtotal * 0.10
total = subtotal + propina + iva

print("\nResumen de la compra:")
print("Productos comprados:")
for plato, cant in ordenes.items():
    print(f"- {plato}: {cant}")

print(f"\nSubtotal: ${subtotal}")
print(f"Propina (5%): ${propina}")
print(f"IVA (10%): ${iva}")
print(f"Total a pagar: ${total}") 
#"f" es para formato de texto, se puede usar para las variables dentro de comillas