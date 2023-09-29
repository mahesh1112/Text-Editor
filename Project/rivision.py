import cv2 as cv

img = cv.imread("download.jpg")
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gry = cv.medianBlur(gry ,5)

edges = cv.adaptiveThreshold(gry, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 5)
color = cv.bilateralFilter(img, 9,250, 250)
animated = cv.bitwise_and(color, color, mask= edges)

cv.imshow("Window", animated)
cv.waitKey(0)