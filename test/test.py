import cv2
import sys
import os
from datetime import datetime
import shutil

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
data_dir = parent_dir + '/data/tank/'
train_dir = data_dir + 'train/'
train_finish_dir = data_dir + 'train_finish/'
files = os.listdir(train_dir)

tag = ""
finish_data = []
for file in files:
    img = cv2.imread(train_dir + file)
    # cv2.imshow("original", img)
    # cv2.waitKey(0)

    img_size = img.shape[:2]

    tag += r"""
                <image file='{0}'>
                  <box top='{1}' left='{2}' width='{3}' height='{4}'/>
                </image>""".format(file, 0, 0, img_size[0], img_size[1])
    finish_data.append(file)
    file_name = parent_dir + '/face_detector/xml/image_data_{0}.txt'.format(datetime.now().strftime('%Y%m%d%H%M'))

f = open(file_name, 'w')
f.write(tag)
print("saved")
f.close()
# for data in finish_data:
#     shutil.move(train_dir + data, train_finish_dir + data)
sys.exit()
