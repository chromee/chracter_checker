import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from scripts.movie_to_picture_converter import MovieToPictureConverter
from scripts.delete_similar_picture import SimilarPictureDeleter
from scripts.post_json import PostJson

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OBSERVE_DIR = PROJECT_DIR + "/data/movie/"
CAP_DIR = PROJECT_DIR + "/data/cap/"


def get_ext(filename):
    return os.path.splitext(filename)[-1].lower()

#コピー&ペーストでディレクトにmp4を入れるとopenCVが動画を読み込まないので，ドラッグ&ドロップでmp4を追加する必要がある．(原因不明)
def execute(movie_dir):
    movie_file_name = os.path.splitext(os.path.split(movie_dir)[1])[0]
    img_set_dir = CAP_DIR + movie_file_name + "/"
    img_set_dir = MovieToPictureConverter.convert(movie_dir, img_set_dir)
    SimilarPictureDeleter.delete(img_set_dir, SimilarPictureDeleter.SAFE_MODE)
    files = os.listdir(img_set_dir)
    for file in files:
        PostJson.post(img_set_dir+file)


class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        if get_ext(event.src_path) == ".mp4":
            print("mp4ファイルが作成されました。処理中...")
            execute(event.src_path)
            print("アップロード完了")

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