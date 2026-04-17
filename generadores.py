import tracemalloc

tracemalloc.start()

def generar_ventas():
    with open("ventas_supermercado.csv", "r") as archivo:
        next(archivo)

        for linea in archivo:
            fila = linea.strip().split(",")

            categoria = fila[2]
            precio = float(fila[3])
            cantidad = int(fila[4])

            if categoria == "Alimentos":
                yield precio * cantidad

total = sum(generar_ventas())

memoria = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("Total:", total)
print("Memoria:", memoria)
