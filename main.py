import time
import cv2
import numpy as np
from display import Display

W = 1920//2
H = 1080//2

disp = Display(W, H)
orb = cv2.ORB_create(100)

def process_frame(img):
    img = cv2.resize(img, (W, H))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)

    for corner in corners:
        #u, v = map(lambda x: int(round(x)), corner[0])
        x, y = corner[0]
        cv2.circle(img, (x,y), color=(0,255,0), radius=2)
        
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test2.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
