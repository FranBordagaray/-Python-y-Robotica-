import cv2
import time
captura = cv2.VideoCapture(0)
fps_start_time = 0
fps : 0
 
if not captura.isOpened():
    print("Cannot open camera")
    exit()

while (captura.isOpened()):
    ret, frame = captura.read()
    cv2.putText(frame,"En vivo",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)
    cv2.imshow('webCam',frame)
    if (cv2.waitKey(1) == ord('y')):
        break

captura.release()
cv2.destroyAllWindows()