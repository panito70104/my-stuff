def insertion_sort(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = actual

Numbs = [7, 2, 5, 9, 1, 6]
insertion_sort(Numbs)
print(Numbs)