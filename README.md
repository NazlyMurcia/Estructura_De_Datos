# Laboratorio 1 - Matriz 100.000 x 100.000

Este proyecto crea una matriz de 100.000 x 100.000 y la almacena en disco duro, usando `numpy.memmap` en formato `.npy`.

## Archivos
- `matriz.py`: crea la matriz (llena de números aleatorios entre 0 y 100) y la guarda en disco por bloques, sin cargarla completa en RAM.
- `mostrar.py`: abre la matriz ya creada y permite consultar filas, columnas o rangos específicos sin cargarla completa en memoria.

## Entregable (matriz generada)
Debido a su tamaño (9.31 GB), el archivo no se pudo subir directamente a GitHub.
Descárgalo aquí: [matriz_100000x100000.npy](https://udeaeduco-my.sharepoint.com/:u:/g/personal/lorena_murcia_udea_edu_co/IQBNuCsQmgbtTJhafxQohQPSAdlaucmDqelgdFV-TWD8qUI?e=zw9Npo)

## Cómo correrlo
1. Instala numpy: `pip install numpy`
2. Ejecuta `python matriz.py` para generar la matriz (tarda varios minutos).
3. Ejecuta `python mostrar.py` para consultar filas, columnas o rangos específicos.

## Resultado obtenido
- Forma de la matriz: (100000, 100000)
- Tamaño real en disco: 9.31 GB
- Tiempo de creación: ~745 segundos (~12.4 minutos)
