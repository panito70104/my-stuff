import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
data = pd.read_excel("ventas_ejemplo.xlsx")

# Corregir nombres de columnas
data.columns = ['Vendedor', 'Mes', 'Ventas']

# Verificar contenido
print("Primeras filas:")
print(data.head())

# Suma total de ventas
print("\nSuma total de ventas:", data["Ventas"].sum())

# Promedio por vendedor
print("\nPromedio de ventas por vendedor:")
print(data.groupby("Vendedor")["Ventas"].mean())

# Mes con mayores ventas
mes_mayor = data.groupby("Mes")["Ventas"].sum().idxmax()
print("\nMes con mayores ventas:", mes_mayor)

# Vendedor con más ventas
mejor_vendedor = data.groupby("Vendedor")["Ventas"].sum().idxmax()
print("Mejor vendedor:", mejor_vendedor)

# Gráfica de ventas por vendedor
data.groupby("Vendedor")["Ventas"].sum().plot(kind="bar", title="Ventas por Vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Ventas")
plt.tight_layout()
plt.show()

