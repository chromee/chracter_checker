import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_text(filename):
    return os.path.splitext(filename)[-1].lower()


class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        if get_text(event.src_path) in ('.jpg', '.png', '.txt'):
            print('%s has been created.' % event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        if get_text(event.src_path) in ('.jpg', '.png', '.txt'):
            print('%s has been modified.' % event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
        if get_text(event.src_path) in ('.jpg', '.png', '.txt'):
            print('%s has been deleted.' % event.src_path)

if __name__ in '__main__':
    print(BASE_DIR)
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, BASE_DIR, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()