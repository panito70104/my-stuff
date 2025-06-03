import numpy as np
matriz = np.array([[10, 20, 30], [40, 50, 60 ]]) # Creating a 2D NumPy array
print(np.shape(matriz)) # Shape of the array
print(matriz[1]) # Accessing the second row
print(matriz[:, 2]) # Accessing the third element of all rows
print(matriz[0, 1]) # Accessing the second  element of the first row