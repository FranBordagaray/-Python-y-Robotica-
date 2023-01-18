import cv2
import numpy as np
img = cv2.imread("Imagenes/cubo.jpg",1)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
blueBajo = np.array([90,50,70] ,np.uint8)
blueAlto = np.array([128,255,255] ,np.uint8)
maskBlue = cv2.inRange(img2, blueBajo, blueAlto)
maskBluevis = cv2.bitwise_and(img2, img,mask = maskBlue)
cv2.imshow("Original",img)
cv2.imshow("maskBlue",maskBlue)
cv2.imshow("maskBluevis",maskBluevis)
cv2.waitKey(0)
cv2.destroyAllWindows

#me detecta los colores azules, pero cuando imprime la imagen solo me la da en verde, lo prore con varios combinaciones.