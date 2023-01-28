import cv2

cap = cv2.VideoCapture('rtsp://admin01:admin213@192.168.0.167/stream1')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break