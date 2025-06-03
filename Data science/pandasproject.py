import pandas as pd
data = pd.read_csv("mejores_estudiantes.csv")
print(data.head(5))
print("Promedio matemáticas:", data["Matematicas"].mean())
print("Promedio historia:", data["Historia"].mean())
print("Promedio ciencias:", data["Ciencias"].mean())
# Agregar una nueva fila con los promedios
promedios = {
    "Nombre": "Promedio",
    "Matematicas": data["Matematicas"].mean(),
    "Historia": data["Historia"].mean(),
    "Ciencias": data["Ciencias"].mean()
}
data = pd.concat([data, pd.DataFrame([promedios])], ignore_index=True)
data["promedio"] = data[["Matematicas", "Historia", "Ciencias"]].mean(axis=1)
data.to_csv("notas_estudiantes.csv", index=False)

print(data["promedio"] >= 85)

df = pd.DataFrame(data)
df_order_by_mean = df.sort_values(by="promedio", ascending=False)

# Ordenar estudiantes por su promedio de forma descendente
df_order_by_mean = df.sort_values(by="promedio", ascending=False)
print(df_order_by_mean)

# Calcular el promedio de notas por grado
promedio_por_grado = df.groupby("Grado")[["Matematicas", "Historia", "Ciencias", "promedio"]].mean()
print(promedio_por_grado)

# Guardar un nuevo CSV con los estudiantes cuyo promedio sea mayor o igual a 85
mejores_estudiantes = df[df["promedio"] >= 85]
mejores_estudiantes.to_csv("mejores_estudiantes.csv", index=False)