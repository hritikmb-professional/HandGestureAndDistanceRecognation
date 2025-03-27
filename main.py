import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)

# Estimate distance based on bounding box size
def estimate_distance(bbox_width, bbox_height, frame_width):
    avg_size = (bbox_width + bbox_height) / 2
    normalized_size = avg_size / frame_width
    distance = int(100 - (normalized_size * 100))
    return max(10, distance)  # Minimum distance set to 10cm

# Recognize hand gestures
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    if thumb_tip.y < index_tip.y and thumb_tip.y < middle_tip.y and thumb_tip.y < ring_tip.y:
        return "Thumbs Up"
    if thumb_tip.y > index_tip.y and thumb_tip.y > middle_tip.y and thumb_tip.y > ring_tip.y:
        return "Thumbs Down"
    if (index_tip.y < thumb_tip.y and middle_tip.y < thumb_tip.y) and (ring_tip.y > index_tip.y and pinky_tip.y > index_tip.y):
        return "Peace"

    return "Unknown"

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Flip for natural interaction
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    frame_height, frame_width, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get bounding box around hand
            x_min = y_min = float("inf")
            x_max = y_max = float("-inf")

            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame_width), int(landmark.y * frame_height)
                x_min, y_min = min(x, x_min), min(y, y_min)
                x_max, y_max = max(x, x_max), max(y, y_max)

            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Estimate distance and recognize gesture
            distance = estimate_distance(x_max - x_min, y_max - y_min, frame_width)
            gesture = recognize_gesture(hand_landmarks.landmark)

            # Display gesture and distance
            text = f"{gesture} | Distance: {distance}cm"
            cv2.putText(frame, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
