import numpy as np
import cv2 as cv
import mediapipe as mp #Mediapipe é feito para a captura de imagens e vídeos, e também para a detecção de mãos, rosto, pose, etc.


maos = mp.solutions.hands
linhas = mp.solutions.drawing_utils
desenho_linhas = mp.solutions.drawing_styles

hands = maos.Hands(
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=2,
)

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame. Exiting...")
        break

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            linhas.draw_landmarks(
                frame,
                hand_landmarks,
                maos.HAND_CONNECTIONS,
                desenho_linhas.get_default_hand_landmarks_style(),
                desenho_linhas.get_default_hand_connections_style(),
            )

    cv.imshow("frame", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

hands.close()
cap.release()
cv.destroyAllWindows()