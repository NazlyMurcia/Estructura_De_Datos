import numpy as np
import os
import time

FILAS = 100_000
COLUMNAS = 100_000
DTYPE = 'int8'
NOMBRE_ARCHIVO = "matriz_100000x100000.npy"

bytes_por_elemento = np.dtype(DTYPE).itemsize
tamano_total_gb = (FILAS * COLUMNAS * bytes_por_elemento) / (1024**3)
print(f"La matriz ocupará aproximadamente {tamano_total_gb:.6f} GB en disco.")

inicio = time.time()

matriz = np.lib.format.open_memmap(NOMBRE_ARCHIVO, dtype=DTYPE, mode='w+', shape=(FILAS, COLUMNAS))

TAMANO_BLOQUE = 1000
for inicio_fila in range(0, FILAS, TAMANO_BLOQUE):
    fin_fila = min(inicio_fila + TAMANO_BLOQUE, FILAS)
    bloque = np.random.randint(0, 100, size=(fin_fila - inicio_fila, COLUMNAS), dtype=DTYPE)
    matriz[inicio_fila:fin_fila, :] = bloque
    print(f"Progreso: fila {inicio_fila}/{FILAS}")

matriz.flush()

fin = time.time()
print(f"Matriz creada y guardada en '{NOMBRE_ARCHIVO}'")
print(f"Tiempo total: {(fin - inicio):.4f} segundos")

tamano_real_gb = os.path.getsize(NOMBRE_ARCHIVO) / (1024**3)
print(f"Tamaño real del archivo en disco: {tamano_real_gb:.6f} GB")

print("\n--- Muestra de la matriz (primeras 5 filas x 5 columnas) ---")
matriz_lectura = np.load(NOMBRE_ARCHIVO, mmap_mode='r')
print(f"Forma de la matriz leída: {matriz_lectura.shape}")
print(matriz_lectura[:5, :5])
