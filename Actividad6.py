import cv2
cap = cv2.VideoCapture("Imagenes/video.mp4")


while (cap.isOpened()):
    ret, frame = cap.read()
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    largo = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps= str(fps)
    ancho = str(ancho)
    largo = str(largo)
    cv2.putText(frame, "Fps: "+fps, (0, 700), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255255, 0, 255), 2)
    cv2.putText(frame, "Ancho: "+ancho, (0, 663), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
    cv2.putText(frame, "Largo: "+largo, (0, 626), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
    if ret == True:
        cv2.imshow("Frame", frame)
        if (cv2.waitKey(1) == ord('y')):
            break
    else: break

cap.release()
cv2.destroyAllWindows()