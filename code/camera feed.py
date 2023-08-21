import cv2
import time

cam = cv2.VideoCapture(0)#initialize camera
time.sleep(1)

while True:
    _,img = cam.read() #read the camera
    cv2.imshow("cameraFeed", img) #displaying the output
    key = cv2.waitKey(1) & 0xFF #it shows that the key is valued
    if key == ord("q"): #if q is pressed then it closes its displaying page
        break

cam.release() #releases the camera
cv2.destroyAllWindows()
