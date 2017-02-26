import cv2
import os
import sys

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
img_dir = project_dir + '/data/test/front/finish/'


def flip_image(flip_code):
    files = os.listdir(img_dir)
    for file in files:
        if file == '.DS_Store' or file == "flip":
            continue
        img = cv2.imread(img_dir + file)
        img = cv2.flip(img, flip_code)
        name, ext = os.path.splitext(file)
        file_name = file
        if flip_code == 0:
            file_name = name + "_flip_xAxis" + ext
        elif flip_code == 1:
            file_name = name + "_flip_yAxis" + ext
        elif flip_code == -1:
            file_name = name + "_flip_xyAxis" + ext
        cv2.imwrite(img_dir + "flip/" + file_name, img)


flip_image(0)
flip_image(1)
flip_image(-1)

sys.exit()