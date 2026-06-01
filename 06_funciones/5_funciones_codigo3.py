import random


def tirar_dados():
    return random.randint(2, 12)


def pedir_respuesta():
    print("\nIngresa tu predicción")
    print("1. Número par")
    print("2. Número impar")
    print("3. Salir")
    return int(input("Opción: "))


def imprimir_resultado(numero, prediccion):

    es_par = numero % 2 == 0

    print("\nNúmero de los dados:", numero)

    if es_par and prediccion == 1:
        print("Ganaste")

    elif not es_par and prediccion == 2:
        print("Ganaste")

    else:
        print("Perdiste")



while True:

    numero = tirar_dados()
    prediccion = pedir_respuesta()

    if prediccion == 3:
        print("\nGracias por jugar")
        break

    imprimir_resultado(numero, prediccion)