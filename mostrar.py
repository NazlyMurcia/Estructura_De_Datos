Aquí tienes mostrar.py documentado, siguiendo la misma lógica:

python
"""
Laboratorio 1 - Lectura y verificación de la matriz de 100.000 x 100.000

Este script permite consultar la matriz ya creada (por matriz.py) sin
necesidad de cargarla completa en memoria RAM. Sirve como "entregable"
para demostrar que el archivo generado sí contiene una matriz real,
con su forma correcta, y para verificar su contenido bajo demanda
(por ejemplo, si el profesor pide ver una fila o columna específica).
"""

import numpy as np
import time
import os

NOMBRE_ARCHIVO = "matriz_100000x100000.npy"

# ------------------------------------------------------------
# Verificamos primero que el archivo exista en la carpeta actual,
# para evitar un error confuso si no se ha descargado todavía.
# ------------------------------------------------------------
if not os.path.exists(NOMBRE_ARCHIVO):
    print(f"No se encontró el archivo '{NOMBRE_ARCHIVO}' en esta carpeta.")
    print("Verifica que lo hayas descargado y ubicado junto a este script.")
else:
    inicio = time.time()

    # --------------------------------------------------------
    # OPTIMIZACIÓN EN LA LECTURA:
    # mmap_mode='r' abre el archivo en modo lectura sin cargar los
    # 10.000 millones de valores en RAM. Solo se leen del disco los
    # datos puntuales que se piden (una fila, una columna, un bloque),
    # justo cuando se solicitan.
    #
    # Como el archivo está en formato .npy, la forma (shape) de la
    # matriz queda guardada dentro del propio archivo. Por eso numpy
    # la reconoce automáticamente como una matriz de 100.000 x 100.000,
    # sin que nosotros tengamos que indicarlo manualmente.
    # --------------------------------------------------------
    matriz = np.load(NOMBRE_ARCHIVO, mmap_mode='r')
    print(f"Forma de la matriz: {matriz.shape}")

    # --------------------------------------------------------
    # Mostrar la primera fila completa.
    # Al pedir solo matriz[0, :], numpy lee del disco únicamente
    # esos 100.000 valores, no la matriz completa.
    # --------------------------------------------------------
    print("\nPrimera fila completa:")
    print(matriz[0, :])

    # Primeros 20 valores de esa misma fila, para una vista más corta.
    print("\nPrimeros 20 valores de la fila 0:")
    print(matriz[0, :20])

    # Primeros 20 valores de la primera columna.
    print("\nPrimera columna (primeros 20 valores):")
    print(matriz[:20, 0])

    # Bloque pequeño (5x5) desde el inicio de la matriz,
    # usado como muestra representativa del contenido generado.
    print("\nBloque 5x5 desde el inicio:")
    print(matriz[:5, :5])

    print(f"\nTiempo total de lectura: {time.time() - inicio:.4f} segundos")
