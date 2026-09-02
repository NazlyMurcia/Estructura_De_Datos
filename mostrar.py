import numpy as np

matriz = np.load("matriz_100000x100000.npy", mmap_mode='r')

print(f"Forma de la matriz: {matriz.shape}")

print("\nPrimera fila completa:")
print(matriz[0, :])

print("\nPrimeros 20 valores de la fila 0:")
print(matriz[0, :20])

print("\nPrimera columna (primeros 20 valores):")
print(matriz[:20, 0])

print("\nBloque 5x5 desde el inicio:")
print(matriz[:5, :5])
