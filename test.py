import os
import sys

import dlib
from skimage import io

import cv2

cascade = cv2.CascadeClassifier("./haarcascades/lbpcascade_animeface.xml")
detector = dlib.simple_object_detector("./face_detector/detector.svm")

cap = cv2.VideoCapture("./GJ-bu OP.mp4")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter('output.avi', fourcc,
    20,
    (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
     int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        dets = detector(img)
        faces = cascade.detectMultiScale(frame,
                                         scaleFactor = 1.1,
                                         minNeighbors = 4,
                                         minSize = (24, 24))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        for d in dets:
            cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
        out.write(frame)
    else:
        break
out.release()
