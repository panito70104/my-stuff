from sklearn.neural_network import MLPClassifier
import numpy as np

# Datos de entrada (X) y salida esperada (y) para una compuerta lógica OR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

# Crear
modelo = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', max_iter=10000)
modelo.fit(X, y)

predicciones = modelo.predict(X)
print("Predicciones:", predicciones)
 #resultados esperados: [0 1 1 1]