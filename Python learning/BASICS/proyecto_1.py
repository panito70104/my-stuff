def registrar_estudiantes():
    base_de_datos = {}

    while True:
        nombre = input("Ingrese el nombre del estudiante (o escriba 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            print("Saliendo del registro de estudiantes.")
            break

        try:
            edad = int(input("Ingrese la edad del estudiante: "))
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            continue

        try:
            nota = float(input("Ingrese la nota del estudiante (0 a 100): "))
            if not (0 <= nota <= 100):
                print("Error: La nota debe estar entre 0 y 100.")
                continue
        except ValueError:
            print("Error: La nota debe ser un número válido.")
            continue

        base_de_datos[nombre] = [edad, nota]
        print("Estudiante registrado:", {nombre: [edad, nota]})

    print("\nBase de datos completa:")
    print("Estudiantes que aprobaron (nota mayor a 60):")
    for estudiante, datos in base_de_datos.items():
        if datos[1] > 60:  # Condición para filtrar notas mayores a 60
            print(f"{estudiante}: Edad = {datos[0]}, Nota = {datos[1]}")

    # Calcular el promedio de las notas
    if base_de_datos:
        total_notas = sum(datos[1] for datos in base_de_datos.values())
        promedio = total_notas / len(base_de_datos)
        print(f"\nEl promedio de las notas ingresadas es: {promedio:.2f}")
    else:
        print("\nNo se ingresaron estudiantes, no se puede calcular el promedio.")

registrar_estudiantes()
