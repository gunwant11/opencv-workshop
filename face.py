import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    r, frame = cap.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if r== False:
        continue
    faces= face_cascade.detectMultiscale(grey_frame,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("video frame", frame)
        key_p = cv2.waitKey(1) & 0Xff 
        if key_p == ord('n'):
            break
    cap.release()
    cv2.destroyAllWindows()
    