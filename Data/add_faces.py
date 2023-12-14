import cv2

faces_data =[]
video = cv2.VideoCapture(0)         #Video capture object
facesdetect = cv2.CascadeClassifier('/Users/apple/Face recognation/Data/haarcascade_frontalface_default.xml') # accessing faces have change(copy path) in other devices
count = 0
nameID = str(input("Enter Your name: ")).lower()
path = '/Users/apple/Face recognation/Data/images/'+nameID   #path to store data
isExists = os.path.exists(path)
if isExists:
    print("Name Already Taken")
    nameID = str(input("Enter your name again: "))
else:
    os.makedirs(path)

while True:
    ret, frame = video.read()
    cv2.imshow("frame",frame)       #Showing the frame
    faces =facesdetect.detectMultiScale(frame, 1.3,5)           #Detectfaces with thrash holder value
    for (x,y,w,h) in faces:         #Iterating through the coordinate form the face variable 
        count += 1
        crop_image = frame[y:yh, x=x+w, :]


        cv2.imwrite(name, frame[y:y+h,x:x+w])    #cutting tge frame
        cv2.recantgle(frame, (x,y),(x+w,y+h), (50,50,255),1)    #Seeing the face with coordinates, color and thickness
    k = cv2.waitKey(1)              #keyboard binding for breakig the loop
    if k == ord('q') or len(faces_data) ==100:
        break

video.release()                     #releasing video
cv2.destroyAllWindows()


