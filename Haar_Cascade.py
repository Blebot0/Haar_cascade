import numpy as np
import cv2


cap = cv2.VideoCapture(-1)

cap.set(3, 800)
cap.set(4, 600)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(cap.isOpened()):
    ret, frame  = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv4.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]


        cv2.imshow("output", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()