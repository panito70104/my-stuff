def clasificar_imc(peso,altura):
    imc =  peso / (altura ** 2)
    if imc < 18.5:
        resultado = "Bajo peso"
    elif 18.5 <= imc < 25:
        resultado = "Peso normal"
    elif 25 <= imc < 30:
        resultado = "Sobrepeso"
    elif imc >= 30:
        resultado = "Obesidad"
    return f"Tu IMC es {round(imc, 2)}. Clasificación: {resultado}"

# Prueba
print(clasificar_imc(900, 1.75))
