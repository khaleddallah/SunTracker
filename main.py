import cv2
import time
from sun_tracking import * 

cam = cv2.VideoCapture(0)
mar=10

while True:
    _, frame = cam.read()
    ref0,cur0,image0 = sun_track(frame)

    #run controller 
    res=controller(ref0,cur0,mar)
    print(res)

    #display controller rectanlge
    controller_show(res['x'],res['y'],mar,image0)

    cv2.imshow("Image", image0)

    #close when ESC pressed
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break



cam.release()

cv2.destroyAllWindows()
