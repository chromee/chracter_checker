import cv2
import os

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
movie_dir = project_dir + '/data/gj-bu/movie/'
file_name = "GJ-bu OP.mp4"
cap = cv2.VideoCapture(movie_dir + file_name)
index = 1

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(project_dir+"/data/movie/"+"GJ-bu OP "+"{0:08d}".format(index)+".jpg", frame)
        index += 1
    else:
        break


class Abc:
    def puts(self):
        print(self)
