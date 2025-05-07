from ultralytics import YOLO
import cv2

# Cargar el modelo entrenado
model = YOLO("runs/detect/train4/weights/best.pt")

# Activar la cámara (0 es la cámara por defecto)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Hacer la predicción
    results = model(frame)

    # Dibujar los resultados sobre el frame
    annotated_frame = results[0].plot()

    # Mostrar el resultado en una ventana
    cv2.imshow("Detección en Vivo", annotated_frame)

    # Salir si se presiona la tecla ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
