import cv2
import time
from sun_tracking import * 



cam = cv2.VideoCapture(1)

print(cam.get(cv2.CAP_PROP_FPS))





while True:
    ret, frame = cam.read()
    ref0,cur0 = sun_track(frame)

    #run controller 
    res=controller(ref0,cur0,10)
    print(res)

    if not ret:
        break

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break



cam.release()

cv2.destroyAllWindows()
