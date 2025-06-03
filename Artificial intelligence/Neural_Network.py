import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neurona(x1, x2, w1, w2, bias):
    z = x1 * w1 + x2 * w2 + bias
    salida = sigmoid(z)
    return salida

# Entradas y pesos
x1 = 1
x2 = 2
w1 = 0.3
w2 = 0.8
bias = -0.1

resultado = neurona(x1, x2, w1, w2, bias)
print("Salida de la neurona:", resultado)
