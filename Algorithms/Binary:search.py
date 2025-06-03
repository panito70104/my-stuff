def busqueda_binaria(arr, objetivo):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

Numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 6
if objetivo in Numbs:
    print(f"El número {objetivo} se encuentra en la posición {busqueda_binaria(Numbs, objetivo)}")
    