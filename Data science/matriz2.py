import numpy as np
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Creating a 2D NumPy array
print(np.diag(matriz))  # Accessing the diagonal elements
print("Primera fila", np.sum(matriz[0]))  # Sum of all elements in the first row
print("Segunda fila", np.sum(matriz[1]))  # Sum of all elements in the second row
print("Tercera fila", np.sum(matriz[2]))  # Sum of all elements in the third row
print("Primera columna", np.sum(matriz[:, 0]))  # Sum of all elements in the first column
print("Segunda columna", np.sum(matriz[:, 1]))  # Sum of all elements in the second column
print("Tercera columna", np.sum(matriz[:, 2]))  # Sum of all elements in the third column
print("Numero mayor de la matriz", np.max(matriz))  # Maximum value in the matrix