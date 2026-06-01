print("Escribe tu nombre")
nombre = input()

print("Escribe tu edad")
edad = int(input())

if nombre == "Rodrigo" and edad > 20:
    print("Saludos Rodrigo, eres un adulto")
elif nombre == "Rodrigo" and edad <= 20:
    print("Saludos Rodrigo, eres un joven")
else:
    print("Saludos")