import cv2

faces_data =[]
video = cv2.VideoCapture(0)         #Video capture object
facesdetect = cv2.CascadeClassifier('/Users/apple/Face recognation/Data/haarcascade_frontalface_default.xml') # accessing faces have change(copy path) in other devices

while True:
    ret, frame = video.read()
    cv2.imshow("frame",frame)       #Showing the frame
    grey =cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)      #Convert into GreyScale to Bgr to work properly 
    face =facesdetect.detectMultiScale(grey, 1.3,5)           #Detectfaces with thrash holder value
    for (x,y,w,h) in faces:         #Iterating through the coordinate form the face variable 
        crop_image = frame[y:yh, x=x+w, :]
        resized_img = cv2.resize(crop_img, (50,50))
        if len(faces_data)<= and i%10 ==0:
        faces_data.append(resized_img)
        cv2.recantgle(frame, (x,y),(x+w,y+h), (50,50,255),1)    #Seeing the face with coordinates, color and thickness
    k = cv2.waitKey(1)              #keyboard binding for breakig the loop
    if k == ord('q') or len(faces_data) ==100:
        break

video.release()                     #releasing video
cv2.destroyAllWindows()


