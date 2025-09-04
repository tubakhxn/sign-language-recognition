import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Define a simple gesture classifier (placeholder for demo)
def classify_gesture(landmarks):
    # Example: If thumb is up, return 'A', else 'Unknown'
    if landmarks:
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        if thumb_tip.y < index_tip.y:
            return 'A'  # Example: Thumb up
    return 'Unknown'

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    gesture = 'No hand detected'
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = classify_gesture(hand_landmarks.landmark)
    # Display gesture
    cv2.putText(frame, f'Sign: {gesture}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    # Watermark
    cv2.putText(frame, 'Made by Tuba', (10, h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,255), 2)
    cv2.imshow('Sign Language Recognition', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
