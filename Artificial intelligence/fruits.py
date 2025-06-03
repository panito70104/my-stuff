import numpy as np
from sklearn.neural_network import MLPClassifier

# X = [peso, tamaño]
X = np.array([
    [150, 7],   # Manzana
    [170, 8],   # Manzana
    [140, 6],   # Manzana
    [120, 5],   # Manzana
    [200, 12],  # Plátano
    [210, 13],  # Plátano
    [190, 11],  # Plátano
    [220, 14]   # Plátano
])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])  # 0 = manzana, 1 = plátano

# Crear y entrenar el modelo
modelo = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', max_iter=10000, random_state=42)
modelo.fit(X, y)
# Probar el modelo
predicciones = modelo.predict(X)
print("Predicciones:", predicciones)
# Resultados esperados: [0 0 0 0 1 1 1 1]

# Probar con un nuevo ejemplo
nuevo_ejemplo = np.array([[160, 9]])  # Un ejemplo de fruta
prediccion_nuevo = modelo.predict(nuevo_ejemplo)
print("Predicción para el nuevo ejemplo:", prediccion_nuevo)
print("Probabilidades:", modelo.predict_proba(nuevo_ejemplo))
