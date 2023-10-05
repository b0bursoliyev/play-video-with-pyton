import cv2
import glob
import numpy as np
#if you are opening your device's camera, you use cv2.VideoCapture(0)
video = cv2.VideoCapture(0)
#if you are opening your video in the path, you use way to your video
path = 'your_path/video'
video = glob.glob(path)
while video.isOpened():
    _,rasm = video.read()
    cv2.imshow("Video",rasm)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
