#!/usr/bin/env python3
import pyperclip

from dialog.dialog_manager import show
from keyevent.key_event_listener import listen
from ocr.ocr_manager import ocr
from screencapture.screen_capture_manager import capture_screen
from translator.google_translator import translate

config = {"copy_to_clipboard": False}


def on_shortcut_triggered():
    image_path = capture_screen()
    text = ocr(image_path)
    if config["copy_to_clipboard"]:
        pyperclip.copy(text)
    result = translate(text)
    show(text, result)


if __name__ == '__main__':
    listen(on_shortcut_triggered)
