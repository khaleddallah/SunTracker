import cv2
from imutils import contours
import imutils


def sun_track(img_path):
    #read image and convert it to gray
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #GaussianBlur for image 
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # threshold the image to reveal light regions in the blurred image
    threshold_value=int(blurred.max())-3
    print(threshold_value)
    thresh = cv2.threshold(blurred, threshold_value , 255, cv2.THRESH_BINARY)[1]


    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)


    # find the contours in the mask, then sort them from left to right
    cnts = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #draw hull Rectangle
    x,y,w,h = cv2.boundingRect(cnts[0])
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    #get center and draw small rectangle in it
    m=cv2.moments(cnts[0])
    cx=int(m['m10']/m['m00'])
    cy=int(m['m01']/m['m00'])
    print (cx,' - ',cy)
    cv2.rectangle(image,(cx-1,cy-1),(cx+1,cy+1),(0,0,255),2)

    # show the output image
    cv2.imshow("Image", image)
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)
