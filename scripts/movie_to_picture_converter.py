import cv2
import os
import unicodedata


class MovieToPictureConverter:
    @staticmethod
    def convert(movie_dir, save_dir):

        file_name = os.path.splitext(os.path.split(movie_dir)[1])[0]
        cap = cv2.VideoCapture(movie_dir)
        file_index = 1

        if is_include_japanese(file_name):
            tmp_file_name = "tmp"
            tmp_save_dir = get_rename_last_dir(save_dir, tmp_file_name)

            if not os.path.exists(tmp_save_dir):
                os.mkdir(tmp_save_dir)

            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite("%s%s%s.jpg" % (tmp_save_dir, tmp_file_name, "_{0:06d}".format(file_index)), frame)
                    file_index += 1
                else:
                    break

            correct_save_dir = create_non_overlapping_dir_name(save_dir)
            os.rename(tmp_save_dir, correct_save_dir)
            correct_file_name = os.path.split(correct_save_dir.rstrip("/"))[1]

            files = os.listdir(correct_save_dir)
            file_index = 1
            for file in files:
                before_name = correct_save_dir + file
                after_name = correct_save_dir + correct_file_name + "_{0:06d}.jpg".format(file_index)
                os.rename(before_name, after_name)
                file_index += 1

            if os.path.exists(tmp_save_dir):
                os.rmdir(tmp_save_dir)

            cap.release()
            return correct_save_dir

        else:
            save_dir = create_non_overlapping_dir_name(save_dir)
            os.mkdir(save_dir)
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite("%s%s%s.jpg" % (save_dir, file_name, "_{0:06d}".format(file_index)), frame)
                    file_index += 1
                else:
                    break

            cap.release()
            return save_dir


def is_include_japanese(string):
    for ch in string:
        name = unicodedata.name(ch)
        if "CJK UNIFIED" in name \
                or "HIRAGANA" in name \
                or "KATAKANA" in name:
            return True
    return False


def get_rename_last_dir(dir, string):
    return os.path.split(dir.rstrip("/"))[0] + "/%s/" % string


def create_non_overlapping_dir_name(dir):
    dir_index = 1
    dir_name = os.path.split(dir.rstrip("/"))[1]
    while True:
        if os.path.exists(dir):
            dir = get_rename_last_dir(dir, dir_name + "_{0:03d}".format(dir_index))
            dir_index += 1
        else:
            return dir


