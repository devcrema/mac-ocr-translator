from pathlib import Path
from subprocess import call

screenshot_path = str(Path.home()) + "/.mac-ocr-translator"
screenshot_file_path = screenshot_path + "/screenshot.png"


def capture_screen():
    Path(screenshot_path).mkdir(parents=True, exist_ok=True)
    call(["screencapture", "-x", "-i", screenshot_file_path])
    return screenshot_file_path
