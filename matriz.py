"""
Laboratorio 1 - Creación de una matriz de 100.000 x 100.000
Estudiante: Nazly Lorena Murcia Rojas

Este script resuelve tres problemas clave al trabajar con matrices tan grandes:
1. Consumo excesivo de RAM: nunca se genera la matriz completa en memoria.
2. Escritura lenta a disco: se escribe por bloques de filas, no elemento por elemento.
3. Optimización de almacenamiento/lectura: se usa el tipo de dato más pequeño posible
   y un formato (.npy) que guarda la forma de la matriz junto con los datos.
"""

import numpy as np
import os
import time

# ------------------------------------------------------------
# Configuración de la matriz
# ------------------------------------------------------------
FILAS = 100_000
COLUMNAS = 100_000

# int8 (1 byte por número) se eligió porque es el tipo de dato más pequeño
# disponible en numpy para enteros. Esto reduce el peso final del archivo
# de ~80 GB (float64) a ~9.3 GB, optimizando tanto el espacio en disco
# como el tiempo de escritura.
DTYPE = 'int8'

NOMBRE_ARCHIVO = "matriz_100000x100000.npy"

# ------------------------------------------------------------
# Calculamos cuánto pesará la matriz antes de crearla,
# para verificar que hay espacio suficiente en disco.
# ------------------------------------------------------------
bytes_por_elemento = np.dtype(DTYPE).itemsize
tamano_total_gb = (FILAS * COLUMNAS * bytes_por_elemento) / (1024**3)
print(f"La matriz ocupará aproximadamente {tamano_total_gb:.6f} GB en disco.")

inicio = time.time()

# ------------------------------------------------------------
# SOLUCIÓN AL CONSUMO EXCESIVO DE RAM:
# np.lib.format.open_memmap crea el archivo .npy directamente en disco,
# sin reservar en RAM el espacio para los 10.000 millones de elementos.
# El array "matriz" que obtenemos aquí es solo una referencia que apunta
# al archivo en disco; los datos no viven en memoria todos a la vez.
# ------------------------------------------------------------
matriz = np.lib.format.open_memmap(NOMBRE_ARCHIVO, dtype=DTYPE, mode='w+', shape=(FILAS, COLUMNAS))

# ------------------------------------------------------------
# SOLUCIÓN A LA ESCRITURA LENTA A DISCO:
# En lugar de escribir número por número (extremadamente lento) o intentar
# generar los 10.000 millones de valores de golpe (satura la RAM), se
# procesa la matriz en bloques de 1000 filas. Cada bloque se genera en
# memoria (algo pequeño y manejable) y se escribe de inmediato en su
# posición correspondiente del archivo en disco.
# ------------------------------------------------------------
TAMANO_BLOQUE = 1000
for inicio_fila in range(0, FILAS, TAMANO_BLOQUE):
    fin_fila = min(inicio_fila + TAMANO_BLOQUE, FILAS)
    bloque = np.random.randint(0, 100, size=(fin_fila - inicio_fila, COLUMNAS), dtype=DTYPE)
    matriz[inicio_fila:fin_fila, :] = bloque
    print(f"Progreso: fila {inicio_fila}/{FILAS}")

# flush() fuerza a escribir en disco cualquier dato que el sistema operativo
# aún tenga pendiente en su caché interna, asegurando que el archivo
# quede completo y consistente.
matriz.flush()

fin = time.time()
print(f"Matriz creada y guardada en '{NOMBRE_ARCHIVO}'")
print(f"Tiempo total: {(fin - inicio):.4f} segundos")

# ------------------------------------------------------------
# Verificamos el tamaño real del archivo generado en disco,
# comparándolo con el tamaño estimado calculado al inicio.
# ------------------------------------------------------------
tamano_real_gb = os.path.getsize(NOMBRE_ARCHIVO) / (1024**3)
print(f"Tamaño real del archivo en disco: {tamano_real_gb:.6f} GB")

# ------------------------------------------------------------
# VERIFICACIÓN DEL CONTENIDO GENERADO (entregable):
# Usamos np.load con mmap_mode='r' para abrir el archivo en modo lectura
# SIN cargarlo completo en RAM. Como el formato .npy guarda la forma
# (shape) dentro del propio archivo, no es necesario indicarla manualmente:
# numpy la reconoce automáticamente como una matriz de 100.000 x 100.000,
# no como un arreglo plano de números sin estructura.
# ------------------------------------------------------------
print("\n--- Muestra de la matriz (primeras 5 filas x 5 columnas) ---")
matriz_lectura = np.load(NOMBRE_ARCHIVO, mmap_mode='r')
print(f"Forma de la matriz leída: {matriz_lectura.shape}")
print(matriz_lectura[:5, :5])
