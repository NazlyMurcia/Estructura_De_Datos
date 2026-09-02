# Laboratorio 1 - Matriz 100.000 x 100.000

**Estudiante:** Nazly Lorena Murcia Rojas

Este proyecto crea una matriz de 100.000 x 100.000 y la almacena directamente en disco duro, resolviendo los problemas de consumo de RAM, velocidad de escritura y optimización en el manejo de datos de gran tamaño.

## Archivos del repositorio

- **`matriz.py`**: crea la matriz completa y la guarda en disco en formato `.npy`, llenándola con números aleatorios entre 0 y 99. Incluye comentarios explicando cada decisión técnica.
- **`mostrar.py`**: abre la matriz ya creada y permite consultar filas, columnas o bloques específicos, sin necesidad de cargarla completa en memoria. Sirve como verificación del contenido generado.

## Entregable (matriz generada)

Debido a su tamaño (9.31 GB), el archivo no se pudo subir directamente a GitHub (el límite de GitHub es 100 MB por archivo).
Descárgalo aquí: [matriz_100000x100000.npy](https://udeaeduco-my.sharepoint.com/:u:/g/personal/lorena_murcia_udea_edu_co/IQBNuCsQmgbtTJhafxQohQPSAdlaucmDqelgdFV-TWD8qUI?e=zw9Npo)

## Cómo se resolvieron los problemas planteados

### 1. Consumo excesivo de RAM
Se usó `numpy.memmap` (a través de `np.lib.format.open_memmap`) para crear la matriz. Esta herramienta mapea el archivo directamente al disco: los datos nunca se generan ni se almacenan completos en memoria RAM, sin importar que la matriz tenga 10.000 millones de elementos.

### 2. Escritura lenta a disco
En lugar de escribir número por número (muy lento) o generar todos los valores de una sola vez (imposible por RAM), la matriz se llena **por bloques de 1000 filas**. Cada bloque se genera y se escribe de inmediato en su posición correspondiente del archivo, equilibrando velocidad y uso de memoria.

### 3. Optimización en manipulación, creación, almacenamiento y lectura
- **Creación/almacenamiento**: se usó el tipo de dato `int8` (1 byte por número), el más pequeño disponible para enteros en numpy, reduciendo el archivo final de ~80 GB (con `float64`) a ~9.3 GB.
- **Formato del archivo**: se usó `.npy` en lugar de un binario plano (`.bin`), porque `.npy` guarda la forma (shape) de la matriz dentro del propio archivo. Así, al leerlo, numpy reconoce automáticamente que es una matriz de 100.000 x 100.000, sin necesidad de indicarlo manualmente.
- **Lectura**: se usó `mmap_mode='r'` al cargar el archivo, permitiendo consultar cualquier fila, columna o bloque específico leyendo solo esa porción desde disco, sin cargar la matriz completa en memoria.

## Cómo correrlo

1. Instala numpy: `pip install numpy`
2. Ejecuta `python matriz.py` para generar la matriz (tarda aproximadamente 12 minutos).
3. Ejecuta `python mostrar.py` para consultar filas, columnas o bloques específicos y verificar el contenido generado.

## Resultado obtenido

- Forma de la matriz: (100000, 100000)
- Tamaño real en disco: 9.31 GB
- Tiempo de creación: ~745 segundos (~12.4 minutos)
