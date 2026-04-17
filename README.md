# Manejo de Memoria y Eficiencia en Python

## Integrantes
- Santiago Meneses Vanegas
- Santiago Osorio Anaya
- Maredwin Galindo Lozano

## Descripción
Este proyecto tiene como objetivo analizar el manejo de memoria y la eficiencia en programación utilizando Python.

Se comparan dos enfoques para resolver el mismo problema:
- Uso de listas (menos eficiente)
- Uso de generadores (más eficiente)

El propósito es demostrar cómo la elección de estructuras de datos impacta directamente en el uso de memoria.

---

## Problema
Calcular el total de ventas de la categoría "Alimentos" a partir de un dataset de ventas de supermercado.

---

## Dataset
El dataset se genera directamente en el código para simular un entorno con grandes volúmenes de datos.

Contiene información como:
- Fecha
- Producto
- Categoría
- Precio
- Cantidad
- Ciudad

Esto permite realizar pruebas sin depender de archivos externos.

---

## Tecnologías
- Python
- Librerías utilizadas:
  - tracemalloc (medición de memoria)
  - time (medición de tiempo)

---

## Implementación

Se desarrollaron dos soluciones:

### 1. Uso de listas
- Se carga todo el archivo en memoria
- Se crean estructuras adicionales (listas)
- Mayor consumo de memoria

### 2. Uso de generadores
- Se procesan los datos uno a uno
- No se almacenan todos los datos en memoria
- Menor consumo de memoria

---

## Ejecución

1. Ejecutar el código que genera el dataset
2. Ejecutar el método con listas
3. Ejecutar el método con generadores

Ejemplo:

```bash
python listas.py
python generadores.py
