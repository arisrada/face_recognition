import cv2

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)
text1 = "Person Detected"
text2 = "No Person Detected"
count = 0
while True:
    count = 1
    _,img = cam.read()
    grayImg = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale (grayImg, 1.3, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        faceOnly = grayImg[y:y+h, x:x+w]
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite("%s/%s.jpg" %(path, count), faceOnly)
        count += 1
    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
print("Image Captured Successfully")
cam.release()
cv2.destroyAllWindows()
