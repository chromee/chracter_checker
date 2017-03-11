import cv2
import os
import shutil


class SimilarPictureDeleter:

    SAFE_MODE = 0
    DELETE_MODE = 1

    @staticmethod
    def delete(img_set_dir, mode):
        img_size = (320, 180)
        files = os.listdir(img_set_dir)

        if len(files) == 0:
            print("no file in %s" % img_set_dir)
            return 0

        target_file_name = files[0]
        safe_dir = img_set_dir + "shelter/"
        if not os.path.exists(safe_dir):
            os.mkdir(safe_dir)

        for file in files:
            if file == '.DS_Store' or file == target_file_name:
                continue
            target_img_path = img_set_dir + target_file_name
            target_img = cv2.imread(target_img_path)
            target_img = cv2.resize(target_img, img_size)
            target_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])

            comparing_img_path = img_set_dir + file
            comparing_img = cv2.imread(comparing_img_path)
            comparing_img = cv2.resize(comparing_img, img_size)
            comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])

            ret = cv2.compareHist(target_hist, comparing_hist, 0)

            if ret < 0.95:
                target_file_name = file
            else:
                if mode == SimilarPictureDeleter.SAFE_MODE:
                    shutil.move(comparing_img_path, safe_dir + file)
                elif mode == SimilarPictureDeleter.DELETE_MODE:
                    os.remove(comparing_img_path)
