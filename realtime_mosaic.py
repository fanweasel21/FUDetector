import cv2
import numpy as np
import time
import HandTrackingModule as htm

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

detector = htm.handDetector(maxHands=10)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  #좌우대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    midfinger = detector.findHands(frame)
    print("Number of Middle Fingers detected: " + str(midfinger))





cap.release()
cv2.destroyAllWindows()



