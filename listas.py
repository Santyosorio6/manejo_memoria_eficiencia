import tracemalloc
import time

tracemalloc.start()
inicio = time.time()

archivo = open("ventas_supermercado.csv", "r")
next(archivo)

datos = []

for linea in archivo:
    fila = linea.strip().split(",")
    datos.append(fila)

archivo.close()

ventas = []

for fila in datos:
    if fila[2] == "Alimentos":
        precio = float(fila[3])
        cantidad = int(fila[4])
        ventas.append(precio * cantidad)

total = sum(ventas)

fin = time.time()
memoria = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("Total:", total)
print("Memoria lista:", memoria)
print("Tiempo:", fin - inicio)
