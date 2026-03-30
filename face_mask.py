import cv2
import numpy as np

# Load face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

def detect_mask(face_img):
    # Convert to HSV
    hsv = cv2.cvtColor(face_img, cv2.COLOR_BGR2HSV)
    
    # Define mask color range (blue/green masks)
    lower = np.array([80, 50, 50])
    upper = np.array([140, 255, 255])
    
    mask = cv2.inRange(hsv, lower, upper)
    ratio = cv2.countNonZero(mask) / (face_img.size / 3)
    
    if ratio > 0.15:
        return "Mask", (0, 255, 0)
    else:
        return "No Mask", (0, 0, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        
        label, color = detect_mask(face)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    cv2.imshow("Face Mask Detector", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()