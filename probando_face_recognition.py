import cv2
import face_recognition
import datetime

# Imagen a comparar - Miguel
image_miguel = cv2.imread("Images/avatarMFR.jpg")
face_loc_miguel = face_recognition.face_locations(image_miguel)[0]
face_encodings_miguel = face_recognition.face_encodings(image_miguel, known_face_locations=[face_loc_miguel])[0]

# Imagen a comparar - Patsy
image_patsy = cv2.imread("Images/PATSY.jpeg")
face_loc_patsy = face_recognition.face_locations(image_patsy)[0]
face_encodings_patsy = face_recognition.face_encodings(image_patsy, known_face_locations=[face_loc_patsy])[0]

# Imagen a comparar - Carmen
image_carmen = cv2.imread("Images/CARMEN.jpeg")
face_loc_carmen = face_recognition.face_locations(image_carmen)[0]
face_encodings_carmen = face_recognition.face_encodings(image_carmen, known_face_locations=[face_loc_carmen])[0]

# Imagen a comparar - Grecia
image_grecia = cv2.imread("Images/GRECIA.jpeg")
face_loc_grecia = face_recognition.face_locations(image_grecia)[0]
face_encodings_grecia = face_recognition.face_encodings(image_grecia, known_face_locations=[face_loc_grecia])[0]

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
    if ret == False: 
        break
    frame = cv2.flip(frame, 1)

    if not person_detected:
        face_locations = face_recognition.face_locations(frame, model="hog")
        if face_locations:
            for face_location in face_locations:
                face_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
                result_miguel = face_recognition.compare_faces([face_encodings_miguel], face_encodings)
                result_patsy = face_recognition.compare_faces([face_encodings_patsy], face_encodings)
                result_carmen = face_recognition.compare_faces([face_encodings_carmen], face_encodings)
                result_grecia = face_recognition.compare_faces([face_encodings_grecia], face_encodings)

                if result_miguel[0]:
                    # Nombre de la persona - Miguel
                    name = "Mike"
                    # Fecha y hora actual
                    current_time = datetime.datetime.now()
                    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    # Crear o abrir el archivo txt para agregar el nombre, la fecha y la hora
                    with open("detected_faces.txt", "a") as file:
                        file.write(f"{name} - {date_time}\n")
                    print(f"{name} ingreso a las {date_time}")
                    
                    person_detected = True  # Actualizar la variable para indicar que la persona ha sido detectada
                elif result_patsy[0]:
                    # Nombre de la persona - Patsy
                    name = "Patsy Delgado"
                    # Fecha y hora actual
                    current_time = datetime.datetime.now()
                    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    # Crear o abrir el archivo txt para agregar el nombre, la fecha y la hora
                    with open("detected_faces.txt", "a") as file:
                        file.write(f"{name} - {date_time}\n")
                    print(f"{name} ingreso a las {date_time}")
                    
                    person_detected = True  # Actualizar la variable para indicar que la persona ha sido detectada
                elif result_carmen[0]:
                    # Nombre de la persona - Carmen
                    name = "Carmen Sandoval"
                    # Fecha y hora actual
                    current_time = datetime.datetime.now()
                    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    # Crear o abrir el archivo txt para agregar el nombre, la fecha y la hora
                    with open("detected_faces.txt", "a") as file:
                        file.write(f"{name} - {date_time}\n")
                    print(f"{name} ingreso a las {date_time}")
                    
                    person_detected = True  # Actualizar la variable para indicar que la persona ha sido detectada
                elif result_grecia[0]:
                    # Nombre de la persona - Grecia
                    name = "Grecia Villar"
                    # Fecha y hora actual
                    current_time = datetime.datetime.now()
                    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    # Crear o abrir el archivo txt para agregar el nombre, la fecha y la hora
                    with open("detected_faces.txt", "a") as file:
                        file.write(f"{name} - {date_time}\n")
                    print(f"{name} ingreso a las {date_time}")
                    
                    person_detected = True  # Actualizar la variable para indicar que la persona ha sido detectada
               
                    

    # Salir del bucle si la persona ha sido detectada
    if person_detected:
        break

cap.release()
cv2.destroyAllWindows()
