def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
    return arr

Numbs = [7, 2, 5, 9, 1, 6]
bubble_sort(Numbs)
print(Numbs)