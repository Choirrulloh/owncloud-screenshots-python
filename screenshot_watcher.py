import config, time, re, pyperclip
from os.path import split as path_split, join as path_join, isfile
from os import getpid
from pync import Notifier
from owncloud_upload import upload_and_share
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class ScreenShotHandler(PatternMatchingEventHandler):
    patterns=["*.png", "*.jpg", "*.jpeg", "*.gif", "*.tif", "*.tiff", "*.bmp", "*.pict", "*.bpg"]

    def process(self, path):
        link = upload_and_share(path)
        pyperclip.copy(link)
        Notifier.notify('Link copied to clipboard.', title=path_split(path)[-1], group=getpid(), open=link)

    """
    event.event_type
        'modified' | 'created' | 'moved' | 'deleted'
    event.is_directory
        True | False
    event.src_path
        path/to/observed/file
    """
    def on_moved(self, event):
        # Screenshots are moved in by the operating system
        # using a temporary name of the form ".NAME-wwww".
        path_parts = path_split(event.src_path)
        filename = path_parts[-1]
        m = re.search('^\.(.+)-\w{4}$', filename)

        # If the current file matches this naming.
        if m:
            # Get the path of the screenshot-to-be.
            path = path_join(path_parts[0], m.group(1))
            # Wait for it to finish moving (with time out).
            for i in range(1000):
                time.sleep(1)
                if isfile(path):
                    # Process the screenshot.
                    self.process(path)
                    return

    def on_created(self, event):
        self.process(event.src_path)


if __name__ == '__main__':
    #args = sys.argv[1:]
    observer = Observer()
    #observer.schedule(ScreenShotHandler(), path=args[0] if args else '.')
    observer.schedule(ScreenShotHandler(), path=config.SCREENSHOTS_FOLDER)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()