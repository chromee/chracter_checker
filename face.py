import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascades/lbpcascade_animeface.xml')

files_dir = './data/train_datas/'
files = os.listdir(files_dir)

for file in files:
    img = cv2.imread(files_dir + file)
    size = img.shape[:2]
    black = np.zeros((size[0], size[1], 3), np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        lx = x - 10
        ly = y - 20
        lw = w + 20
        lh = h + 20
        cv2.rectangle(img, (lx, ly), (lx + lw, ly + lh), (255, 0, 0), 2)

        roi_color = img[ly:ly + lh, lx:lx + lw]
        black[ly:ly + lh, lx:lx + lw] = roi_color

    cv2.imshow('img', img)
    cv2.imshow('black', black)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
