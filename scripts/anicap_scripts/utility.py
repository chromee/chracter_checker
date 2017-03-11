import os
import unicodedata


class Utility:
    @staticmethod
    def files_rename(file_dir, file_name):
        files = os.listdir(file_dir)
        file_index = 1
        for file in files:
            before_name = file_dir + file
            after_name = file_dir + file_name + "_{0:06d}.jpg".format(file_index)
            os.rename(before_name, after_name)
            file_index += 1

    @staticmethod
    def is_include_japanese(string):
        for ch in string:
            name = unicodedata.name(ch)
            if "CJK UNIFIED" in name \
                    or "HIRAGANA" in name \
                    or "KATAKANA" in name:
                return True
        return False

    @staticmethod
    def get_renamed_last_dir_name(dir, string):
        return os.path.split(dir.rstrip("/"))[0] + "/%s/" % string

    @staticmethod
    def get_non_overlapping_dir(dir):
        dir_index = 1
        dir_name = os.path.split(dir.rstrip("/"))[1]
        while True:
            if os.path.exists(dir):
                dir = Utility.rename_last_dir_name(dir, dir_name + "_{0:03d}".format(dir_index))
                dir_index += 1
            else:
                return dir
