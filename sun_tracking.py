import cv2
from imutils import contours
import imutils
import time


def controller (ref,cur,mar):
    report=dict()
    #x axis
    if(cur[0]<(ref[0]-mar)):
        report['left']=ref[0]-cur[0]
        report['right']=0
        report['x']=False

    elif(cur[0]>(ref[0]+mar)):
        report['left']=0
        report['right']=cur[0]-ref[0]
        report['x']=False

    else:
        report['left']=0
        report['right']=0
        report['x']=True

    #y axis
    if(cur[1]<(ref[1]-mar)):
        report['top']=ref[1]-cur[1]
        report['down']=0
        report['y']=False

    elif(cur[1]>(ref[1]+mar)):
        report['top']=0
        report['down']=cur[1]-ref[1]
        report['y']=False

    else:
        report['top']=0
        report['down']=0
        report['y']=True


    return (report)



#first parameter is image from imread
def sun_track(image):
    cur2=(0,0)
    ref2=(0,0)

    #read image and convert it to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #GaussianBlur for image 
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # threshold the image to reveal light regions in the blurred image
    threshold_value=int(blurred.max())-1
    # print(threshold_value)
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
    try:
        cx=int(m['m10']/m['m00'])
        cy=int(m['m01']/m['m00'])
        cur2=(cx,cy)
        # print (cx,' - ',cy)
        cv2.circle(image,cur2, 10, (0,0,255),3) 
    except:
        pass
        #print("ZeroDivisionError: float division by zero")

    #draw circle in center of frame
    h,w,_=image.shape
    ref2=(w//2,h//2)
    cv2.circle(image, ref2, 10, (255,0,0),3) 


    # show the output image
    cv2.imshow("Image", image)
    cv2.imshow("thresh", thresh)

    return(ref2,cur2)
