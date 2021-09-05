import cv2
import mediapipe as mp
import time


video_var = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils



while True:
    success, image = video_var.read()
    img1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(img1)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                height, width, channels = image.shape
                cx, cy = int(lm.x*width), int(lm.y*height)

                cv2.circle(image, (cx,cy), 10,(255,255,0))
            mpDraw.draw_landmarks(image,handLms, mpHand.HAND_CONNECTIONS)
              

    cv2.imshow("Hand tracker", image)

    cv2.waitKey(1) 
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

video_var.release()
cv2.destroyAllWindows()