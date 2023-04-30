import cv2

img = cv2.imread(r'D:\Users\jains\Pictures\Screenshots\Mri.jpg')
cv2.namedWindow('Elon Musk')

def nothing(x):
    pass

cv2.createTrackbar('lower','Elon Musk',0,255,nothing)
cv2.createTrackbar('upper','Elon Musk',0,255,nothing)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    x = cv2.getTrackbarPos('lower','Elon Musk')
    y = cv2.getTrackbarPos('upper', 'Elon Musk')

    edge = cv2.Canny(gray,x,y)
    cv2.imshow('Elon Musk', edge)

    if cv2.waitKey(1) == 27:
        cv2.destroyAlllWindows()
        break