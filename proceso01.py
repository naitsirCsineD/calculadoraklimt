import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv('archivo.csv')

# Separa los datos en dos DataFrames distintos, uno para cada serie de datos
serie1 = df[df['clase_comun'] == 'serie1']
serie2 = df[df['clase_comun'] == 'serie2']

# Crea la gráfica de líneas utilizando matplotlib
fig, ax = plt.subplots()
ax.plot(serie1['fecha'], serie1['valor'], label='Serie 1')
ax.plot(serie2['fecha'], serie2['valor'], label='Serie 2')

# Agrega títulos y etiquetas de eje
ax.set_title('Comparación de dos series de datos')
ax.set_xlabel('Fecha')
ax.set_ylabel('Valor')

# Agrega una leyenda
ax.legend()

# Muestra la gráfica
plt.show()
