from datetime import datetime

print("***************************")
print("****** Bienvenida a *******")
print("** La tienda de mascotas **")
print("***************************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaro": 25,
    "iguana": 2
}

compras = []

animales_totales = 0

for val in inventario.values():
    animales_totales += val


def mostrar_inventario():

    print()
    print("*** INVENTARIO ***")

    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")

    total = 0

    for valor in inventario.values():
        total += valor

    print()
    print(f"En total tenemos {total} animales")


def mostrar_compras():

    print()
    print("*** COMPRAS REALIZADAS ***")

    for compra in compras:
        print(f"{compra[0]} compró "f"{compra[1]} "f"en la fecha {compra[2]}")


print("Por favor ingresa tu nombre")
nombre = input()

print("Por favor escribe tu apellido")
apellido = input()

nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos", nombre_completo)

while True:

    print("Selecciona la opcion que deseas")
    print("1. Ver inventario")
    print("2. Comprar un animal")
    print("3. Mostrar compras")
    print("4. Salir")

    respuesta = int(input())

    if respuesta == 1:

        mostrar_inventario()

    elif respuesta == 2:

        carrito = []

        while True:

            print("¿Que animal deseas comprar?")
            print("Escribe F para terminar")
            print("Escribe V para ver tu carrito")

            animal = input().lower()

            if animal == "f":break

            if animal == "v":
                print(f"Tu carrito de compras contiene {carrito}")
                continue

            if animal not in inventario:
                print(f"Lo sentimos, no contamos con el animal {animal}")
            elif inventario[animal] == 0:
                print(f"Lo sentimos, no tenemos en existencia el animal {animal}")
            elif animal not in carrito:
                carrito.append(animal)
            else:
                print("Ese animal ya se encuentra en tu carrito")

        print("El contenido de tu carrito es")

        for animal in carrito:

            print(" ", animal)

            inventario[animal] -= 1

        fecha = datetime.now()

        compras.append((nombre_completo,carrito,fecha))

    elif respuesta == 3:

        mostrar_compras()

    elif respuesta == 4:

        print("Gracias por visitar la tienda")
        break