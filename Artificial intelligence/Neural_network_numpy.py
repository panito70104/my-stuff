import numpy as np

# Función sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Entradas (puedes cambiar estos valores para probar)
X = np.array([[200, 0]])  # 1 muestra, 2 características

# Pesos y bias de la capa oculta (2 neuronas)
W1 = np.array([[0.4, 0.3],
               [-0.5, 0.2]])  # (2 entradas, 2 neuronas)
b1 = np.array([-0.1, 0.2])   # Bias para cada neurona

# Calcular activación de la capa oculta
Z1 = np.dot(X, W1) + b1
A1 = sigmoid(Z1)

# Pesos y bias de la capa de salida
W2 = np.array([[0.6], 
               [0.1]])  # (2 neuronas ocultas, 1 salida)
b2 = np.array([0.0])    # Bias para la salida

# Calcular activación de la salida
Z2 = np.dot(A1, W2) + b2
output = sigmoid(Z2)

print("Salida de la red:", output[0][0])
