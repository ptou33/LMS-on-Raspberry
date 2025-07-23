import cv2

stream = True

cap = cv2.VideoCapture(0)  # 0 corrisponde a /dev/video0

if not cap.isOpened():
    print("Errore nell'apertura della webcam")
    exit()

ret, frame = cap.read()
cv2.imwrite("/app/output/test.jpg", frame)

while stream:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
