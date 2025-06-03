import numpy as np
array = np.arange(12) # Creating a 1D NumPy array with values from 0 to 11
matriz = array.reshape(3, 4)  # Reshaping the array into a 2D array with 3 rows and 4 columns
print(matriz)  # Printing the 2D array
print(np.sum(matriz))  # Sum of all elements in the matrix
print(np.mean(matriz))  # Mean of all elements in the matrix
print(matriz[:, 3])  # Accessing the fourth column of the matrix