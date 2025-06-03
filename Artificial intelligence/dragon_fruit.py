import numpy as np
from sklearn.neural_network import MLPClassifier

# X = [peso, tamaño]
X = np.array([
    [50, 3],    # Pequeña
    [60, 4],    # Pequeña
    [70, 5],    # Pequeña
    [150, 7],   # Mediana
    [170, 8],   # Mediana
    [140, 6],   # Mediana
    [120, 5],   # Mediana
    [200, 12],  # Grande
    [210, 13],  # Grande
    [190, 11],  # Grande
    [220, 14]   # Grande
])
y = np.array([0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])  # 0 = pequeña, 1 = mediana, 2 = grande

# Crear y entrenar el modelo
modelo = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', max_iter=1000000000, random_state=42)
modelo.fit(X, y)
# Probar el modelo
predicciones = modelo.predict(X)
print("Predicciones:", predicciones)
# Resultados esperados: [0 0 0 1 1 1 1 2 2 2]

# Probar con un nuevo ejemplo
nuevo_ejemplo = np.array([int(x) for x in input("Introduce el peso y tamaño de la fruta (separados por una coma): ").split(",")])
prediccion_nuevo = modelo.predict(nuevo_ejemplo.reshape(1, -1))
print("Predicción para el nuevo ejemplo:", prediccion_nuevo)
print("Probabilidades:", modelo.predict_proba(nuevo_ejemplo.reshape(1, -1)))