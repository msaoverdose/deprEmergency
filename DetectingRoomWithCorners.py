import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img = cv2.imread("e.png")
img2=img.copy()
img3=img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

corners = cv2.goodFeaturesToTrack(gray3, 90, 0.3, 10)
corners = np.int0(corners)
kose=0  
for i in corners:
    kose += 1
    x, y = i.ravel()
    cv2.circle(img3, (x, y), 10, (0,115,255), -1)
    #cv2.putText(img,"KOSE",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(60,55,55),2)
  
for i, c in enumerate(contours):
    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)

    x1 = random.randint(0,255)
    y2 = random.randint(0,255)
    z3 = random.randint(0,255)

    x, y, w, h = cv2.boundingRect(approx)
    
    center_x = x + int(w / 2)
    center_y = y + int(h / 2)

    cv2.rectangle(img3, (x, y), (x + w, y + h), (x1, y2, z3), 1)
    cv2.putText(img3, "Oda {}".format(i+1), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 43, 255), 3)

n_squares = 8

# Karelerin boyutu
square_size = img.shape[0] // n_squares

# Etiket başlangıç numarası
label_num = 1

# Her bir kare için etiket ekleyin
for i in range(n_squares):
    for j in range(n_squares):
        
        # Karelerin koordinatları
        x = j * square_size
        y = i * square_size
        
        # Köşe noktalarının koordinatları
        corners = np.array([[x, y], [x + square_size, y], [x + square_size, y + square_size], [x, y + square_size]])
        
        # Etiket yazdırma
        label = str(label_num)
        label_num += 1
        x_label = x + square_size // 2
        y_label = y + square_size // 2
        cv2.putText(img, label, (x_label, y_label), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 0, 255), 1, cv2.LINE_AA)
        
        # Kareleri çizme
        cv2.polylines(img, [corners], True, (255, 0, 0), thickness=2)

imagestack = [img,img2,img3]

stacked_img = cv2.hconcat(imagestack)  

cv2.imshow("HOUSE", stacked_img)

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
