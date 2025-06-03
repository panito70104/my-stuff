def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = 6
print(f"El factorial de {n} es {factorial(n)}")