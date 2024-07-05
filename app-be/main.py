#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# help

import matplotlib.pyplot as plt
import numpy as np
import csv
import os

# Obtener la ruta absoluta del directorio raíz del repositorio
directorio_raiz = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa al archivo datos.csv dentro del directorio inbox
input_file = os.path.join(directorio_raiz, 'inbox', 'datos.csv')
output_file = os.path.join(directorio_raiz, 'outbox', 'output.png')
# import pdb; pdb.set_trace()
# Se crean las variables x e y vacias
x = []
y = []
# Se leen las variables
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Saltar la primera fila si hay encabezados
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))


# Se crea la Figura.
plt.figure()
plt.plot(x,y)
plt.show(block=False)
plt.savefig(output_file)
plt.close()
