import cv2


video = cv2.VideoCapture(0) #Video capture object

while True:
    ret, frame = video.read()
    cv2.imshow("frame",frame)   #Showing the frame
    k = cv2.waitKey(1)          #keyboard binding for breakig the loop
    if k == ord('q'):
        break

video.release()                 #releasing video
cv2.destroyAllWindows()


