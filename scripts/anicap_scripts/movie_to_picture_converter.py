import cv2
import os
from scripts.anicap_scripts.utility import Utility


class MovieToPictureConverter:
    @staticmethod
    def convert_en_file(movie_dir, save_dir):
        file_name = os.path.splitext(os.path.split(movie_dir)[1])[0]
        convert(movie_dir, file_name, save_dir)

    @staticmethod
    def convert_jp_name(movie_dir, save_dir):
        convert(movie_dir, "tmp", save_dir)


def convert(movie_dir, file_name, save_dir):
    cap = cv2.VideoCapture(movie_dir)
    file_index = 1
    save_dir = Utility.get_non_overlapping_dir(save_dir)
    os.mkdir(save_dir)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("%s%s%s.jpg" % (save_dir, file_name, "_{0:06d}".format(file_index)), frame)
            file_index += 1
        else:
            break
    cap.release()
