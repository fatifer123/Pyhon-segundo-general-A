# Lista de elementos llave : valor
# Arreglos asociativos

persona = {
    "nombre": "Rodrigo",
    "edad": 800,
    "apellido": "Montemayor"
}

print(persona)

print(persona["apellido"])

persona["apellido"] = "Lozano"

print(persona)

persona["apodo"] = "Ringa Tech"

print(persona)

print(persona.keys())

print(persona.values())

print(persona.items())

for key in persona.keys():
    print(key)

for value in persona.values():
    print(value)

for key, value in persona.items():
    print(f"La llave {key} tiene el valor {value}")

print("apodo" in persona)

print("direccion" in persona)