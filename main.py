import cv2
import time
from sun_tracking import * 

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    ref0,cur0 = sun_track(frame)

    #run controller 
    res=controller(ref0,cur0,10)
    print(res)

    #close when ESC pressed
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break



cam.release()

cv2.destroyAllWindows()
