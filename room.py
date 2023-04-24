import cv2
import numpy as np
import random
img = cv2.imread("a.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i, c in enumerate(contours):
    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)

    x1 = random.randint(0,255)
    y2 = random.randint(0,255)
    z3 = random.randint(0,255)

    x, y, w, h = cv2.boundingRect(approx)

    center_x = x + int(w / 2)
    center_y = y + int(h / 2)

    cv2.rectangle(img, (x, y), (x + w, y + h), (x1, y2, z3), -1)
    cv2.putText(img, "Oda {}".format(i+1), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Ev Şeması", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
