import cv2

#load Camera
cap = cv2.VideoCapture(1)

while True:
    #To get Frame after Frame 
    ret,frame = cap.read()      
    #To show the Frame
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    # to quit
    if key == "s":
        break

cap.release()
cv2.destroyWindow()