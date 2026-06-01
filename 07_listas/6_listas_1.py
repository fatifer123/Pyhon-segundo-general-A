nombres = ["Rodrigo", "Juan", "Pedro", "Santiago", "Jorge", "Raimundo"]

print(nombres)

print("Bienvenidos a la fiesta", nombres[:3])

for i, nombre in enumerate(nombres):
    print(f"Se inscribió {nombre} en la lista con el índice {i}")

print("Lo sentimos", nombres[3:])