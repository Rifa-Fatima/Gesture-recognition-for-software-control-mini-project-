import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)  # 0 for the default camera (you can change this if needed)

while True:
    _, frm= cap.read()
    
    cv2.imshow("Hand Gesture Recognition", frm)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()



import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


frame_rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
results = hands.process(frame_rgb)


if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for landmark in landmarks.landmark:
                x, y, z = landmark.x, landmark.y, landmark.z  # x, y, and z coordinates of each landmark
                



if y > 0.8 and x > 0.2 and x < 0.8:
                    pyautogui.click()  # Perform a click action when a thumbs-up is detected



