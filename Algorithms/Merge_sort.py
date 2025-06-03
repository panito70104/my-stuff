def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        izquierda = arr[:mid]
        derecha = arr[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Fusionar izquierda y derecha
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Elementos restantes
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1
Numbs = [10, 3, 6, 1, 8, 4, 7]
merge_sort(Numbs)
print(Numbs)