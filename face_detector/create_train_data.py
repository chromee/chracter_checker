import cv2
import numpy as np
import sys
import os
from datetime import datetime
import shutil

drawing = False
sx, sy = 0, 0
gx, gy = 0, 0
rectangles = []
ok = False


def draw_circle(event, x, y, flags, param):
    global sx, sy, gx, gy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        sx, sy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if x > 0 and x < img.shape[1]:
            gx = x
        if y > 0 and y < img.shape[0]:
            gy = y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        w = abs(sx - x)
        h = abs(sy - y)
        if w < h * 1.1 and h < w * 1.1:
            rectangles.append([(sx, sy), (x, y)])


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/data/'
train_dir = data_dir + 'train_data/'
train_finish_dir = data_dir + 'train_data_finish/'
files = os.listdir(train_dir)

i = 0
tag = ""
finish_data = []
for file in files:
    rectangles = []
    while True:
        img = cv2.imread(train_dir + file)
        for r in rectangles:
            cv2.rectangle(img, r[0], r[1], (255, 255, 255), 2)

        if drawing:
            w = abs(sx - gx)
            h = abs(sy - gy)
            if w < h * 1.1 and h < w * 1.1:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
            cv2.rectangle(img, (sx, sy), (gx, gy), color, 2)
        cv2.imshow('image', img)

        k = cv2.waitKey(1) & 0xFF
        if k == ord('d'):
            if rectangles:
                rectangles.pop()
        elif k == ord('s'):
            if len(rectangles) > 0:
                for r in rectangles:
                    x = min(r[0][0], r[1][0])
                    y = min(r[0][1], r[1][1])
                    w = abs(r[0][0] - r[1][0])
                    h = abs(r[0][1] - r[1][1])
                tag += r"""
                <image file='{0}'>
                  <box top='{1}' left='{2}' width='{3}' height='{4}'/>
                </image>""".format(file, y, x, w, h)
                finish_data.append(file)
                i += 1
                break
        elif k == ord('q'):
            file_name = './face_detector/xml/image_data_{0}.txt'.format(datetime.now().strftime('%Y%m%d%H%M'))
            f = open(file_name, 'w')
            f.write(tag)
            print("saved")
            f.close()
            for data in finish_data:
                shutil.move(train_dir + data, train_finish_dir + data)
            sys.exit()
