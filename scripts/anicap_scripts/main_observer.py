import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from scripts.anicap_scripts.movie_to_picture_converter import MovieToPictureConverter
from scripts.anicap_scripts.delete_similar_picture import SimilarPictureDeleter
from scripts.anicap_scripts.post_json import PostJson
from scripts.anicap_scripts.utility import Utility

PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), os.pardir))
OBSERVE_DIR = PROJECT_DIR + "/data/movie/"
CAP_DIR = PROJECT_DIR + "/data/cap/"


def get_ext(filename):
    return os.path.splitext(filename)[-1].lower()


# コピー&ペーストでディレクトにmp4を入れるとopenCVが動画を読み込まないので，ドラッグ&ドロップでmp4を追加する必要がある．(原因不明)
def execute(movie_dir):
    movie_file_name = os.path.splitext(os.path.split(movie_dir)[1])[0]
    if Utility.is_include_japanese(movie_file_name):
        tmp_img_set_dir = CAP_DIR + "tmp/"
        MovieToPictureConverter.convert_jp_name(movie_dir, tmp_img_set_dir)
        SimilarPictureDeleter.delete(tmp_img_set_dir, SimilarPictureDeleter.SAFE_MODE)
        img_set_dir = Utility.get_renamed_last_dir_name(tmp_img_set_dir, movie_file_name)
        os.rename(tmp_img_set_dir, img_set_dir)
        Utility.files_rename(img_set_dir, movie_file_name)
        files = os.listdir(img_set_dir)
        for file in files:
            PostJson.post(img_set_dir + file)
    else:
        img_set_dir = CAP_DIR + movie_file_name + "/"
        MovieToPictureConverter.convert_en_file(movie_dir, img_set_dir)
        SimilarPictureDeleter.delete(img_set_dir, SimilarPictureDeleter.SAFE_MODE)
        files = os.listdir(img_set_dir)
        for file in files:
            PostJson.post(img_set_dir+file)


class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if get_ext(event.src_path) == ".mp4":
            print("created mp4 file...")
            execute(event.src_path)
            print("complete!")

if __name__ in '__main__':
    print("start observing "+OBSERVE_DIR)
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, OBSERVE_DIR, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()