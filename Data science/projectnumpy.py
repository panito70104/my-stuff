import numpy as np

Student_notes = np.array([
    [85, 90, 78],
    [88, 76, 92],
    [70, 85, 80],
    [95,100, 98]
])

# Promedio general
print("Promedio general del grupo:", np.mean(Student_notes))

# Promedio por estudiante
promedios_estudiantes = np.mean(Student_notes, axis=1)
print("Promedio por estudiante:", promedios_estudiantes)

# Promedio por actividad
print("Promedio por actividad:", np.mean(Student_notes, axis=0))

# Estudiante con mejor promedio
mejor = np.argmax(promedios_estudiantes)
print("Estudiante con mejor promedio:", mejor + 1, "con un promedio de", promedios_estudiantes[mejor])