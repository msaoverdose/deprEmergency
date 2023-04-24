import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img = cv2.imread("a.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

corners = cv2.goodFeaturesToTrack(gray, 90, 0.5, 10)
corners = np.int0(corners)
kose=0  
for i in corners:
    kose += 1
    x, y = i.ravel()
    cv2.circle(img, (x, y), 10, (0,0,255), -1)
    #cv2.putText(img,"KOSE",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(60,55,55),2)
  
for i, c in enumerate(contours):
    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)

    x1 = random.randint(0,255)
    y2 = random.randint(0,255)
    z3 = random.randint(0,255)

    x, y, w, h = cv2.boundingRect(approx)
    
    center_x = x + int(w / 2)
    center_y = y + int(h / 2)

    cv2.rectangle(img, (x, y), (x + w, y + h), (x1, y2, z3), 3)
    cv2.putText(img, "Oda {}".format(i+1), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 43, 255), 3)
cv2.imshow("HOUSE", img)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
