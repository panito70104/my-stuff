def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i  # Devuelve la posición
    return -1  # Si no se encuentra

Numbs = [10, 3, 6, 1, 8, 4, 7]
objetivo = 6
if objetivo in Numbs:
    print(f"El número {objetivo} se encuentra en la posición {busqueda_lineal(Numbs, objetivo)}")