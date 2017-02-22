import cv2
import os
import shutil

IMG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/data/movie/'
IMG_SIZE = (320, 180)
files = os.listdir(IMG_DIR)
TARGET_FILE = files[0]


def target_hist_val(target_name):
    target_img_path = IMG_DIR + target_name
    target_img = cv2.imread(target_img_path)
    target_img = cv2.resize(target_img, IMG_SIZE)
    target_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])
    return target_hist


print('TARGET_FILE: %s' % TARGET_FILE)


for file in files:
    if file == '.DS_Store' or file == TARGET_FILE:
        continue

    # print('TARGET_FILE: %s' % TARGET_FILE)
    target_hist = target_hist_val(TARGET_FILE)
    comparing_img_path = IMG_DIR + file
    comparing_img = cv2.imread(comparing_img_path)
    comparing_img = cv2.resize(comparing_img, IMG_SIZE)
    comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])

    ret = cv2.compareHist(target_hist, comparing_hist, 0)
    # print(file, "%03.5f"%ret)

    if ret < 0.95:
        TARGET_FILE = file
    else:
        shutil.move(comparing_img_path, IMG_DIR + "test/" + file)
        # os.remove(comparing_img_path)

