import cv2
import numpy as np
video = cv2.VideoCapture(0)

while video.isOpened():
    _,rasm = video.read()
    cv2.imshow("Video",rasm)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
