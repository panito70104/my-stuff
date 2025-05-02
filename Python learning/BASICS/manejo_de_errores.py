def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: División por cero.")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    else:
        return resultado
dividir(10, 0)  # Error: División por cero.
