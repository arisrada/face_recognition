import cv2
img = cv2.imread("sample2.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg, 120,255,cv2.THRESH_BINARY)[1]
cv2.imshow("Threshold image",thresImg)
cv2.imwrite("thresholdImage.jpg", thresImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
