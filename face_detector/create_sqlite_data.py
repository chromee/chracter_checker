import cv2
import numpy as np
import sys
import os
import sqlite3

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
        if 0 < x < img.shape[1]:
            gx = x
        if 0 < y < img.shape[0]:
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

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
img_set_dir = project_dir + '/data/test/front/'

dbname = "face_database.db"
conn = sqlite3.connect(dbname)
db = conn.cursor()

files = os.listdir(img_set_dir)
for file in files:
    rectangles = []
    while True:
        file_dir = img_set_dir + file
        img = cv2.imread(file_dir)

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
                    sql = "insert into images (name, dir, type, box) values (?,?,?,?)"
                    img_type = os.path.split(img_set_dir.rstrip("/"))[1]
                    image = (file, file_dir, img_type, ';'.join([str(i) for i in [x, y, w, h]]))
                    db.execute(sql, image)
                break
        elif k == ord('q'):
            conn.commit()
            conn.close()
            sys.exit()

conn.commit()
conn.close()
sys.exit()
