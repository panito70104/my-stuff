import math
def sigmoid(x):
 return 1 / (1 + math.exp(-x))

#entrance
x1, x2 = 2, -1
#weights

#neuron 1
w11, w12 = 0.4, 0.3
b1 = -0.1
 
#neuron 2

w21, w22 = -0.5, 0.2
b2 = 0.2

#output of hidden layer
z1 = w11 * x1 + w12 * x2 + b1
a1 = sigmoid(z1)

#output of hidden layer
z2 = w21 * x1 + w22 * x2 + b2
a2 = sigmoid(z2)

# Pesos y bias para la salida
w_out1, w_out2 = 0.6, 0.1
b_out = 0

z_final = a1 * w_out1 + a2 * w_out2 + b_out
salida = sigmoid(z_final)

print("Salida de la red:", salida)
