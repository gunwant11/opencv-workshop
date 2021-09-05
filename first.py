import cv2


video_var = cv2.VideoCapture(0)

while True:
    success, img = video_var.read()

    # cv2.circle(img,(200,200), 30,(0,0,255), cv2.FILLED)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cv2.imshow("yo", img_bgr)

    if cv2.waitKey(1) & 0xff == ord('w'):
        break




