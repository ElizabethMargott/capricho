import cv2
import face_recognition
import datetime
import json
import os

# Cargar datos de alumnos desde un archivo JSON
with open("alumnos.json", "r") as file:
    alumnos = json.load(file)

# Inicializar un diccionario para almacenar las codificaciones faciales
face_encodings_dict = {}

for alumno in alumnos:
    image_path = alumno["image_path"]
    if os.path.exists(image_path):
        image = cv2.imread(image_path)
        face_locations = face_recognition.face_locations(image)
        if face_locations:
            face_encodings = face_recognition.face_encodings(image, known_face_locations=[face_locations[0]])[0]
            face_encodings_dict[alumno["name"]] = face_encodings
        else:
            print(f"No se detectó ninguna cara en la imagen: {image_path}")
    else:
        print(f"No se encontró la ruta de la imagen: {image_path}")

# Inicializar la captura de video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Reducir el ancho del fotograma
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Reducir la altura del fotograma

if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

person_detected = False  # Variable para rastrear si la persona ya ha sido detectada

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    if not person_detected:
        face_locations = face_recognition.face_locations(frame, model="hog")
        if face_locations:
            for face_location in face_locations:
                face_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]

                # Comparar la codificación facial con las codificaciones almacenadas
                for name, known_face_encoding in face_encodings_dict.items():
                    results = face_recognition.compare_faces([known_face_encoding], face_encodings)
                    if results[0]:
                        # Fecha y hora actual
                        current_time = datetime.datetime.now()
                        date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                        # Crear o abrir el archivo txt para agregar el nombre, la fecha y la hora
                        with open("detected_faces.txt", "a") as file:
                            file.write(f"{name} - {date_time}\n")
                        print(f"{name} ingreso a las {date_time}")
                        
                        person_detected = True  # Actualizar la variable para indicar que la persona ha sido detectada
                        break
                if person_detected:
                    break

    # Salir del bucle si la persona ha sido detectada
    if person_detected:
        break

cap.release()
cv2.destroyAllWindows()
