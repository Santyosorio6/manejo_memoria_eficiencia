import tracemalloc
import time

tracemalloc.start()
inicio = time.time()

def calcular_ventas():
    archivo = open("ventas_supermercado.csv", "r")
    next(archivo)

    for linea in archivo:
        fila = linea.strip().split(",")

        if fila[2] == "Alimentos":
            precio = float(fila[3])
            cantidad = int(fila[4])
            yield precio * cantidad

    archivo.close()

total = sum(calcular_ventas())

fin = time.time()
memoria = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("Total:", total)
print("Memoria (MB):", memoria / (1024 * 1024))
print("Tiempo:", fin - inicio)
