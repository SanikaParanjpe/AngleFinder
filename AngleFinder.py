import cv2
import math

path = 'angles.jpeg'

img = cv2.imread(path)
pointsList = []


def gradient(point1, point2):
    return (point2[1] - point1[1] )/( point2[0] - point1[0])


def calcAngle(pointsList):
    point1, point2, point3 = pointsList[-3:]
    print(point1, point2, point3)
    m1 = gradient(point1, point2)
    m2 = gradient(point1, point3)
    angleR = math.atan((m2 - m1) / (1 + (m2 * m1)))
    angleD = round(math.degrees(angleR))
    if(angleD <0):
        angleD +=180
    print(angleD)
    cv2.putText(img,str(angleD),(point1[0]-10,point1[1]-10), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        cv2.circle(img, (x, y), 1, (0, 0, 255), cv2.FILLED)

        if(size !=0 and size %3 != 0):
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(255,0,0),2)
        pointsList.append([x, y])
        if len(pointsList) % 3 == 0 and len(pointsList) != 0:
            calcAngle(pointsList)

while True:

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)
