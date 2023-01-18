import cv2
img = cv2.imread("Imagenes/5.png",1)

#Muestra de Imagen
cv2.imshow("Auto",img)
cv2.waitKey(0)
ancho = img.shape[1]
alto = img.shape[0]
print(ancho,alto)
#Recorte de la Imagen
img_out = img[315:355,321:450]
cv2.imshow("Auto",img_out)
cv2.waitKey(0)
cv2.imwrite("patente.png",img_out)







cv2.destroyAllWindows