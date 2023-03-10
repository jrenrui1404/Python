# -*- coding: utf-8 -*-
"""“Introducción al procesamiento de datos con Panda

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vIDfr2STzTYmFKp4N0QTCVJ2kuW85oMn

# Introducción al procesamiento de datos con Panda [This link](https://pandas.pydata.org/)
"""

import matplotlib.pyplot as plt
import pandas as pd

# Diccionario
alumnos = [
    {'nombre': 'Jose', 'edad': 20, 'pais_nacimiento': 'España', 'nota_media': 7},
    {'nombre': 'Dani', 'edad': 13, 'pais_nacimiento': 'España', 'nota_media': 9},
    {'nombre': 'Jose', 'edad': 50, 'pais_nacimiento': 'España', 'nota_media': 9},
    {'nombre': 'Juani', 'edad': 42, 'pais_nacimiento': 'España', 'nota_media': 7},
    {'nombre': 'Elena', 'edad': 20, 'pais_nacimiento': 'España', 'nota_media': 10}
]

# Dataframe
df = pd.DataFrame(alumnos)

# DF (Nombre y Nota)
df_notas = df[['nombre', 'nota_media']]

# Compruebo que la nota sea mayor de 5 para que esté aprobada
df_notas_aprobadas = df_notas[df_notas['nota_media'] >= 5]

# Cargo fichero
df_fichero = pd.read_csv('sample_data/california_housing_test.csv')

# 20 líneas
print(df_fichero.head(20))

# 20 últimas líneas
print(df_fichero.tail(20))

# Información
print(df_fichero.info())

# Sub-dataframe
df_veinte_hab = df_fichero[df_fichero['total_bedrooms'] < 20]

# Gráfica1
x_values = df_veinte_hab['total_bedrooms'].unique()
y_values = df_veinte_hab['total_bedrooms'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.title('Gráfica 1')
plt.xlabel('Habitaciones')
plt.ylabel('Nº habitaciones')
plt.grid()
plt.savefig('grafica1.png')
plt.show()
plt.close('all')


# Gráfica2
df_veinte_hab.plot(kind='bar', x='population', y='total_bedrooms', label='total_bedrooms')
plt.title('Gráfica 2')
plt.show()