
import cv2
import numpy as np
# Load an image
image = cv2.imread("2.png")
# Changing the colour-space
#image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))); 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray=cv2.inRange(gray,0,254)
gray=cv2.bitwise_not(gray)
#element = np.array(((1,0,0,0,1),(0,1,0,1,0),(0,0,1,0,0),(0,1,0,1,0),(1,0,0,0,1)),dtype=np.uint8)

#for i in range(0,6):
#    gray = cv2.erode(gray,element)
gray = gray.astype('uint8')
cv2.imwrite("binary.png",gray)
gray = (255-gray)
# Find edges

# Find Contours
contours, hierarchy = cv2.findContours(gray ,2, 1)
# Find Number of contours
print("Number of Contours is: " + str(len(contours)))
# Draw yellow border around two contours
#cv2.drawContours(image, contours, 0, (0, 230, 255), 6)
for i in range(0,len(contours)):
    blank=np.zeros(shape=image.shape, dtype=np.uint8)
    cv2.drawContours(blank, contours, i, (255, 255, 255), 1)
    x,y,w,h = cv2.boundingRect(contours[i])
    #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    letter = blank[y:y+h,x:x+w]
    cv2.imwrite("train/cnt"+str(i)+".jpg", letter)
cv2.drawContours(image, contours, -1, (0,0, 255), 6)
cv2.imshow("win",image)
cv2.waitKey(0)   
# Show the image with contours

