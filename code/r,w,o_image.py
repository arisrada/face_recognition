import cv2
img = cv2.imread("sample1.png")
cv2.imshow("Red rose", img)
cv2.imwrite("Rose.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
