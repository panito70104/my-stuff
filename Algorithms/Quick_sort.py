def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

Nums = [10, 3, 6, 1, 8, 4, 7]
Nums = quick_sort(Nums)  # Guarda el resultado ordenado en Nums
print(Nums)